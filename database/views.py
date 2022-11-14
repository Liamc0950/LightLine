
#Boilerplate
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView

from .models import *
from .forms import *

from projects.models import *
from accounts.models import *

import tempfile
from django.views.generic.edit import FormView


#CSV
import csv

@login_required
#Database feature view
def databaseView(request):
    #try to get the active project, then get all the instruments linked to active project
    try:
        activeProject = Project.objects.get(projectCreator=request.user.profile, active=True)
        instrumentList = Instrument.objects.filter(project=activeProject)
    #if no active project, set instrumentList to empty queryset
    except:
        activeProject = Project.objects.none()
        instrumentList = Instrument.objects.none()

    #get all projects created by user
    projects = Project.objects.filter(projectCreator=request.user.profile)


    context={
        'activeProject': activeProject,
        'instrumentList' : instrumentList,
        'projects' : projects,
    }

    return render(request, "database/databaseDatatable.html", context)

class ImportCSVLWFormView(FormView):
    form_class = CSVForm
    template_name = 'database/upload.html'  # Replace with your template.
    success_url = '/database'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        #Get active project
        activeProject = Project.objects.get(projectCreator= self.request.user.profile, active=True)

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                for chunk in f.chunks():
                    Instrument.addInstrumentsFromCSV(chunk, activeProject)


            return self.form_valid(form)
        else:
            return self.form_invalid(form)


#Delete Cue - deletes given cue (designated by parent of delete button)
@login_required
def instumentDelete(request, instrumentID):
    insturment = Instrument.objects.get(id=instrumentID)
    insturment.delete()
    return HttpResponseRedirect('/database')
