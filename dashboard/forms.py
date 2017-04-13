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

class AddPeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ('id', )

class TopicEditForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('periods', 'image', )

class TopicTrEditForm(forms.ModelForm):
    class Meta:
        model = TopicTr
        fields = ('name', )

class AddTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('periods', )


class ContentEditForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('topic', 'image', )

class ContentTrEditForm(forms.ModelForm):
    class Meta:
        model = ContentTr
        fields = ('title', 'text')

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
        fields = ('company', 'address', 'city', 'country', 'postal_code', 'description', 'avatar')
        widgets = {'country': CountrySelectWidget()}

