from django import forms
from betterforms.multiform import MultiModelForm
from django.contrib.auth.models import User
from django_countries.widgets import CountrySelectWidget

from .models import Period, PeriodTr, Topic, TopicTr, Content, ContentTr, Profile


class PeriodEditForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ('image', )

class PeriodTrEditForm(forms.ModelForm):
    class Meta:
        model = PeriodTr
        fields = ('name', )

class EditPeriodExtendedMultiForm(MultiModelForm):
    form_classes = {
        'period_tr': PeriodTrEditForm,
    }

class AddPeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ('id', )


class TopicEditForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('image', )

class TopicTrEditForm(forms.ModelForm):
    class Meta:
        model = TopicTr
        fields = ('language', 'name')

class EditTopicExtendedMultiForm(MultiModelForm):
    form_classes = {
        'topic': TopicEditForm,
        'topic_tr': TopicTrEditForm,
    }

class AddTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('periods', )


class ContentEditForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('image', )

class ContentTrEditForm(forms.ModelForm):
    class Meta:
        model = ContentTr
        fields = ('language', 'title', 'text')

class EditContentExtendedMultiForm(MultiModelForm):
    form_classes = {
        'content': ContentEditForm,
        'content_tr': ContentTrEditForm,
    }

class AddContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('topic', 'id', )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('company', 'address', 'city', 'country', 'postal_code', 'description', )
        widgets = {'country': CountrySelectWidget()}