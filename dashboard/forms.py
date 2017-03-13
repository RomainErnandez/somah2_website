from django import forms
from betterforms.multiform import MultiModelForm

from .models import Period, PeriodTr, Topic, TopicTr, Content, ContentTr


class PeriodEditForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ('image', )

class PeriodTrEditForm(forms.ModelForm):
    class Meta:
        model = PeriodTr
        fields = ('language', 'name')

class EditPeriodExtendedMultiForm(MultiModelForm):
    form_classes = {
        'period': PeriodEditForm,
        'period_tr': PeriodTrEditForm,
    }

class AddPeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ('id', 'image',)


class TopicEditForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('periods', 'image', )

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
        fields = ('periods', 'image',)


class ContentEditForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('topic', 'image', )

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
        fields = ('topic', 'id', 'image',)