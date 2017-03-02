from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.views.generic import FormView

from home.models import Period, Language, PeriodTr, Topic, TopicTr, Content, ContentTr
from somah2_website.local_settings import TRELLO_API_KEY

def dashboard(request):
    return render(request, 'home/dashboard.html', { 'TRELLO_API_KEY':TRELLO_API_KEY })

def view_period(request, period_id):
    try:
        period = Period.objects.get(id=period_id)
    except Exception as e:
        raise Http404
    else:
        return HttpResponse("period: " + str(period.id))

def user(request):
    return render(request, template_name='home/user.html')

def notifications(request):
    return render(request, template_name='home/notifications.html')

def table(request):
    all_languages = Language.objects.all().order_by('country') # country_code
    all_flags = list()
    for language in all_languages:
        all_flags.append(language.country.flag)

    all_periods = Period.objects.all()
    all_periods_trs = list() # [periods_trs_for_period1, periods_trs_for_period2..]
    for period in all_periods:
        all_periods_trs.append(PeriodTr.objects.filter(period=period).order_by('language__country')) # list
    all_periods_extended = zip(all_periods, all_periods_trs)

    all_topics = Topic.objects.all()
    all_topics_trs = list() # [topics_trs_for_topic1, topics_trs_for_topic2..]
    for topic in all_topics:
        all_topics_trs.append(TopicTr.objects.filter(topic=topic).order_by('language__country')) # list
    all_topics_extended = zip(all_topics, all_topics_trs)

    all_contents = Content.objects.all()
    all_contents_trs = list()
    for content in all_contents:
        all_contents_trs.append(ContentTr.objects.filter(content=content).order_by('language__country'))  # list
    all_contents_extended = zip(all_contents, all_contents_trs)

    return render(request, 'home/table.html', { 'all_flags':all_flags, 'all_periods_extended':all_periods_extended,
            'all_topics_extended':all_topics_extended, 'all_contents_extended':all_contents_extended })


def remove_period(request, period_id):
    return view_period(request, period_id)

class EditPeriodView(CreateView):
    model = Period
    fields = '__all__'
    template_name = 'home/edit_period.html'

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, 'home/edit_period_success.html', {'news': self.object})

