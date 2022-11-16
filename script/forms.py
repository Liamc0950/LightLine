from script.models import Script
from django import forms

class UploadScriptForm(forms.ModelForm):
    class Meta:
        model = Script
        fields = ('scriptName', 'pdf',)
