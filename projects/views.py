#Boilerplate
from __future__ import unicode_literals
from django.urls import reverse_lazy



from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.shortcuts import render

from django.http import HttpResponseRedirect


from .models import *
from .forms import *


@login_required
def index(request):

    # Get projects assigned to user
    projects = Project.objects.filter(projectCreator=request.user.profile)
    activeProject = Project.objects.get(active=True)

    # Create context array
    context = {
        'projects' : projects,
        'activeProject' : activeProject,
    }

    # Dashboard Page
    return render(request, 'projects/projects.html', context)



@method_decorator(login_required, name='dispatch')
class ProjectCreateView(CreateView):
    template_name = 'projects/projectCreate.html'
    form_class = ProjectCreateForm
    success_message = 'Success: Project was created.'
    #On success, return to dashboard
    success_url = reverse_lazy('projects:projectIndex')
    

    def get_initial(self, *args, **kwargs):
        initial = super(ProjectCreateView, self).get_initial(**kwargs)
        initial['projectCreator'] = self.request.user.profile
        initial['active'] = True
        return initial

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # Sets all projects to active=False 
        userProjects = Project.objects.filter(projectCreator= self.request.user.profile, active=True)
        for project in userProjects:
            project.active = False
            project.save()
        return super().form_valid(form)


#Delete Project - deletes given project(designated by parent of delete button)
def projectDelete(request, projectID):
    project = Project.objects.get(id=projectID)
    project.delete()
    return HttpResponseRedirect('/projects/')


# @login_required
def switchActiveProject(request):
    if request.method == "POST":
        #get all active projects created by user
        userProjects = Project.objects.filter(projectCreator=request.user.profile, active=True)
        #deactivate all active projects
        for project in userProjects:
            project.active = False
            project.save()
        #Activate selected project
        projID = request.POST.get('proj', '/')
        proj = Project.objects.get(id=projID)
        proj.active = True;
        proj.save()

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
