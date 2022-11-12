#Boilerplate
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


from .models import *
#from cueList.models import *
#from landing.models import Profile


# Create your views here.

@login_required
#Notes feature view
def notes(request):

    #get the active project
    activeProject = Project.objects.get(projectCreator=request.user.profile, active=True)
    # #get the active cueList and cues
    # activeCueList = CueList.objects.get(project = activeProject, active = True)
    # #get all cues where cueList's project is the activeProject and cueList is active
    # activeCues = Cue.objects.order_by('eosCueNumber').filter(cueList__project = activeProject, cueList__active = True)
    # #get all activeProject cue Lists
    # projectCueLists = CueList.objects.filter(project = activeProject)

    #get assignees
    pe = Assignee.objects.get(id=1)
    designer = Assignee.objects.get(id=2)
    programmer = Assignee.objects.get(id=3)


    # #get all projects assigned to user - for sidebar
    projects = Project.objects.filter(projectCreator=request.user.profile)

    # #get all activeProject workNotes
    activeWorkNotes = WorkNote.objects.filter(project=activeProject, completed = False)
    completedWorkNotes = WorkNote.objects.filter(project=activeProject, completed = True)
    peWorkNotes = WorkNote.objects.filter(project=activeProject, assignedTo = pe, completed = False)
    designerWorkNotes = WorkNote.objects.filter(project=activeProject, assignedTo = designer, completed = False)
    programmerWorkNotes = WorkNote.objects.filter(project=activeProject, assignedTo = programmer, completed = False)

    #get all assignee options
    assignees = Assignee.objects.filter()

    template = loader.get_template('notes/notes.html')

    context = {
        'cueList': None,
        'activeProject': activeProject,
        'projects' : projects,
        'projectCueLists' : None,
        'activeCueList' : None,
        'activeWorkNotes' : activeWorkNotes,
        'completedWorkNotes' : completedWorkNotes,
        'peWorkNotes' : peWorkNotes,
        'designerWorkNotes' : designerWorkNotes,
        'programmerWorkNotes' : programmerWorkNotes,
        'assignees' : assignees,
    }

    return HttpResponse(template.render(context, request))


#Create Work Note with no modal
@login_required
def createWorkNote(request):
    #try to get the active project, then get all the cues in cueList linked to active project
    try:
        activeProject = Project.objects.get(projectCreator=request.user.profile, active=True)
    #if no active project, set to none
    except:
        activeProject = Project.objects.none()


    WorkNote.objects.create(project=activeProject, createdBy=request.user.profile)
    
    return HttpResponseRedirect('/notes')


#Update Work Note - for use with inline "editable" elements
@csrf_exempt
def updateWorkNote(request):
    id=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    workNote=WorkNote.objects.get(id=id)
    if type=="noteText":
        workNote.noteText=value

    if type == "channelList":
        workNote.channelList = value

    if type == "cue":
        workNote.cue = value


    if type == "createdBy":
        workNote.createdBy = value

    if type == "assignedTo":
        workNote.assignedTo = Assignee.objects.get(id=value)

    if type == "priority":
        workNote.priority = value

    if type == "forGroup":
        if value == "t" or value == "T" or value == "true" or value == "True":
            workNote.forGroup = True
        if value == "f" or value == "F" or value == "false" or value == "False":
            workNote.forGroup = False
        else:
            pass


    workNote.save()
    return JsonResponse({"success":"Updated Work Note"})


#Mark note as completed
def completeNote(request, noteID):
    note = WorkNote.objects.get(id=noteID)
    note.complete()
    return HttpResponseRedirect('/notes')
