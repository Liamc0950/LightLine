from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from projects.models import Project

@login_required
def index(request):

    # Get projects assigned to user
    projects = Project.objects.filter(projectCreator=request.user.profile)
    activeProject = Project.objects.get(active=True)

    # Create context array
    context = {
        'projects' : projects,
        'activeProject': activeProject,
    }

    # Dashboard Page
    return render(request, 'dashboard/dashboard.html', context)
