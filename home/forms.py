from django import forms
from betterforms.multiform import MultiModelForm

from home.models import Period, PeriodTr


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