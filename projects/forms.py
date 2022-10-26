from django.forms import ModelForm
from .models import Project
from django import forms

# Create form
class ProjectCreateForm(ModelForm):
     class Meta:
         model = Project
         exclude = ['lastUpdate']
         widgets = {'projectCreator': forms.HiddenInput(),
                    'active' : forms.HiddenInput()}
# Edit form
class ProjectChangeForm(ModelForm):
     class Meta:
         model = Project
         fields = ['showName', 'showNameShort', 'venue']
         exclude = ['lastUpdate']
         widgets = {'projectCreator': forms.HiddenInput(),
                    'active' : forms.HiddenInput()}
