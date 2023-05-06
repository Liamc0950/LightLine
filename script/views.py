from django.shortcuts import render

from projects.models import *
from accounts.models import *
from cueList.models import *
from script.models import *
from script.forms import *

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect


@login_required
def scriptView(request):

    # Get projects assigned to user
    projects = Project.objects.filter(projectCreator=request.user.profile)
    activeProject = Project.objects.get(active=True, projectCreator=request.user.profile)

    projectCueLists = CueList.objects.filter(project=activeProject)
    
    try:
        script = str(Script.objects.get(project=activeProject, active=True).pdf)
    except:
        script = ""

    # Create context array
    context = {
        'projects' : projects,
        'activeProject': activeProject,
        'projectCueLists': projectCueLists,
        'script': script,
    }

    # Dashboard Page
    return render(request, 'script/script.html', context)


@login_required
def ScriptUploadView(request):

    # Get active project
    activeProject = Project.objects.get(active=True, projectCreator=request.user.profile)


    if request.method == 'POST':
        form = UploadScriptForm(request.POST,request.FILES)
        if form.is_valid():
            instance = Script(pdf=request.FILES['pdf'])
            instance.project = activeProject
            instance.activate()
            instance.save()
            return HttpResponseRedirect('/script')

    else:
        form = UploadScriptForm()
        context = {
            'form':form,
        }
    return render(request, 'script/upload.html', context)

