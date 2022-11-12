
#Boilerplate
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView

from .models import *

from projects.models import *
from accounts.models import *

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

#IMPORT CSV FROM LIGHTWRIGHT
def importLWCSV(request):
    activeProject = Project.objects.get(lightingDesigner= request.user.profile, active=True)
    csv = open('lightlineapp/testLWExport.csv', 'r')  

    Instrument.addInstrumentsFromCSV(csv, activeProject)

    csv.close() 

    return HttpResponseRedirect('/database')


