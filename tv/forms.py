from django import forms
from tv.models import tvTime


class ActiveForm(forms.Form):
    #is tv show active - meaning currently on and not a finale
    active = forms.BooleanField()