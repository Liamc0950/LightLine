from accounts.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput

from django import forms
from .models import *

from bootstrap_modal_forms.forms import BSModalModelForm


class WorkNoteForm(BSModalModelForm):
    class Meta:
        model = WorkNote
        exclude = ['lastUpdate']
        widgets = {'cueList': forms.HiddenInput()}
