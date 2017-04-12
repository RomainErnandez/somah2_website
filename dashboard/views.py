import os

from django.contrib import messages
from django.db import transaction
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic import DeleteView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dashboard.serializers import PeriodSerializer, PeriodTrSerializer, LanguageSerializer, TopicSerializer, \
    TopicTrSerializer, ContentSerializer, ContentTrSerializer
from .forms import AddPeriodForm, AddContentForm, \
    AddTopicForm, UserForm, ProfileForm, PeriodTrEditForm, TopicTrEditForm, \
    ContentTrEditForm, PeriodEditForm, ContentEditForm, TopicEditForm
from .models import Period, Language, PeriodTr, Topic, TopicTr, Content, ContentTr
from somah2_website.settings import MEDIA_ROOT


def dashboard(request):
    files = os.listdir(os.path.join(MEDIA_ROOT, 'pdf/'))
    return render(request, 'dashboard/dashboard.html', { 'files':files})

def view_period(request, period_id):
    try:
        period = Period.objects.get(id=period_id)
    except Exception as e:
        raise Http404
    else:
        return HttpResponse("period: " + str(period.id))

@transaction.atomic
def user(request):
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['username']=request.user.username
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('user')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'dashboard/user.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def notifications(request):
    return render(request, template_name='dashboard/notifications.html')

def table(request):
    all_languages = Language.objects.all().order_by('country') # country_code
    all_flags = list()
    for language in all_languages:
        all_flags.append(language.country.flag)
    zipped_languages_flags = list(zip(all_languages, all_flags)) # zip is an iterator so we need a list for the 3 tables

    all_periods = Period.objects.all().order_by('id')
    all_periods_trs = list() # [periods_trs_for_period1, periods_trs_for_period2..]
    for period in all_periods:
        all_periods_trs.append(PeriodTr.objects.filter(period=period).order_by('language__country')) # list
    all_periods_extended = zip(all_periods, all_periods_trs)

    all_topics = Topic.objects.all().order_by('periods__id', 'id')
    all_topics_trs = list() # [topics_trs_for_topic1, topics_trs_for_topic2..]
    for topic in all_topics:
        all_topics_trs.append(TopicTr.objects.filter(topic=topic).order_by('language__country')) # list
    all_topics_extended = zip(all_topics, all_topics_trs)

    all_contents = Content.objects.all().order_by('topic__periods__id', 'topic_id', 'id')
    all_contents_trs = list()
    for content in all_contents:
        all_contents_trs.append(ContentTr.objects.filter(content=content).order_by('language__country'))  # list
    all_contents_extended = zip(all_contents, all_contents_trs)

    return render(request, 'dashboard/table.html', {'zipped_languages_flags':zipped_languages_flags, 'all_periods_extended':all_periods_extended,
            'all_topics_extended':all_topics_extended, 'all_contents_extended':all_contents_extended })

class AddPeriodExtendedView(CreateView):
    model = Period
    form_class = AddPeriodForm
    template_name = 'dashboard/add_period_extended.html'

    def form_valid(self, form):
        form.save()
        id = form['id'].value()
        period = Period.objects.get(id=id)
        all_languages = Language.objects.all().order_by('country')  # country_code
        for language in all_languages:
            period_tr = PeriodTr.objects.create(language=language, period=period)
        return redirect('add_period_extended_success')

class EditPeriodTrView(UpdateView):
    model = PeriodTr
    form_class = PeriodTrEditForm
    template_name = 'dashboard/edit_period_tr.html'
    success_url = reverse_lazy('edit_period_success')

    def get_object(self, queryset=None):
        period_id = self.kwargs.get('period_id')
        country_code = self.kwargs.get('language')
        language = Language.objects.get(country=country_code)
        return PeriodTr.objects.get(period__id=period_id, language=language)

class RemovePeriodExtendedView(DeleteView):
    model = Period
    template_name = 'dashboard/remove_period_extended.html'
    success_url = reverse_lazy('remove_period_extended_success')

    def get_object(self, queryset=None):
        id = self.kwargs.get('pk')
        related_topics = Topic.objects.filter(periods__id=id) # only 1 and the period to be deleted
        related_topics.delete()
        return Period.objects.get(id=id)

class AddTopicExtendedView(CreateView):
    model = Topic
    form_class = AddTopicForm
    template_name = 'dashboard/add_topic_extended.html'

    def form_valid(self, form):
        # save new topic
        topic = form.save()

        # create topic_tr for this topic for each language
        all_languages = Language.objects.all().order_by('country')  # country_code
        for language in all_languages:
            topic_tr = TopicTr.objects.create(language=language, topic=topic)
        return redirect('add_topic_extended_success')

class EditTopicTrView(UpdateView):
    model = TopicTr
    form_class = TopicTrEditForm
    template_name = 'dashboard/edit_topic_tr.html'
    success_url = reverse_lazy('edit_topic_success')

    def get_object(self, queryset=None):
        topic_id = self.kwargs.get('topic_id')
        country_code = self.kwargs.get('language')
        language = Language.objects.get(country=country_code)
        return TopicTr.objects.get(topic__id=topic_id, language=language)

class RemoveTopicExtendedView(DeleteView):
    model = Topic
    template_name = 'dashboard/remove_topic_extended.html'
    success_url = reverse_lazy('remove_topic_extended_success')

    def get_object(self, queryset=None):
        id = self.kwargs.get('pk')
        related_contents = Content.objects.filter(topic__id=id).delete()
        return Topic.objects.get(id=id)

class AddContentExtendedView(CreateView):
    model = Content
    form_class = AddContentForm
    template_name = 'dashboard/add_content_extended.html'

    def form_valid(self, form):
        content = form.save()
        all_languages = Language.objects.all().order_by('country')  # country_code
        for language in all_languages:
            content_tr = ContentTr.objects.create(language=language, content=content)
        return redirect('add_content_extended_success')

class EditContentTrView(UpdateView):
    model = ContentTr
    form_class = ContentTrEditForm
    template_name = 'dashboard/edit_content_tr.html'
    success_url = reverse_lazy('edit_content_success')

    def get_object(self, queryset=None):
        content_id = self.kwargs.get('content_id')
        country_code = self.kwargs.get('language')
        language = Language.objects.get(country=country_code)
        return ContentTr.objects.get(content__id=content_id, language=language)

class RemoveContentExtendedView(DeleteView):
    model = Content
    template_name = 'dashboard/remove_content_extended.html'
    success_url = reverse_lazy('remove_content_extended_success')

    def get_object(self, queryset=None):
        id = self.kwargs.get('pk')
        return Content.objects.get(id=id)

class PeriodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Period.objects.all().order_by('id')
    serializer_class = PeriodSerializer

class PeriodTrViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PeriodTr.objects.all().order_by('period__id', 'language__country')
    serializer_class = PeriodTrSerializer

class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Topic.objects.all().order_by('periods__id', 'id')
    serializer_class = TopicSerializer

class TopicTrViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TopicTr.objects.all().order_by('topic__id', 'language__country')
    serializer_class = TopicTrSerializer

class ContentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Content.objects.all().order_by('topic__periods__id', 'topic__id', 'id')
    serializer_class = ContentSerializer

class ContentTrViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ContentTr.objects.all().order_by('content__id', 'language__country')
    serializer_class = ContentTrSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Language.objects.all().order_by('country')
    serializer_class = LanguageSerializer

@api_view(['GET'])
def get_all_association_period_topic(request):
    all_association_period_topic = list()
    all_topics = Topic.objects.all()
    for topic in all_topics:
        related_periods = topic.get_periods().split("\n")
        for period in related_periods:
            all_association_period_topic.append(
                {
                     "period_id": int(period),
                    "topic_id": topic.id
                }
            )
    return Response(all_association_period_topic)

class EditPeriodView(UpdateView):
    model = Period
    form_class = PeriodEditForm
    template_name = 'dashboard/edit_period.html'
    success_url = reverse_lazy('edit_period_success')

    def get_object(self, queryset=None):
        period_id = self.kwargs.get('period_id')
        return Period.objects.get(id=period_id)

class EditTopicView(UpdateView):
    model = Topic
    form_class = TopicEditForm
    template_name = 'dashboard/edit_topic.html'
    success_url = reverse_lazy('edit_topic_success')

    def get_object(self, queryset=None):
        topic_id = self.kwargs.get('topic_id')
        return Topic.objects.get(id=topic_id)

class EditContentView(UpdateView):
    model = Content
    form_class = ContentEditForm
    template_name = 'dashboard/edit_content.html'
    success_url = reverse_lazy('edit_content_success')

    def get_object(self, queryset=None):
        content_id = self.kwargs.get('content_id')
        return Content.objects.get(id=content_id)