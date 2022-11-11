from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from projects.models import Project
from cueList.models import *
@login_required
def index(request):

    # Get projects assigned to user
    projects = Project.objects.filter(projectCreator=request.user.profile)
    try:
        activeProject = Project.objects.get(active=True)
    except:
        activeProject = None
    projectCueLists = CueList.objects.filter(project=activeProject)
    # Create context array
    context = {
        'projects' : projects,
        'activeProject': activeProject,
        'projectCueLists': projectCueLists,
    }

    # Dashboard Page
    return render(request, 'dashboard/dashboard.html', context)
