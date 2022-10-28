from django.urls import path
from . import views

app_name = 'projects'


urlpatterns = [
    #project add view
    path('', views.index, name='projectIndex'),
    path('projectCreate', views.ProjectCreateView.as_view(), name='projectCreate'),
    path('projectDelete/<int:projectID>', views.projectDelete, name='projectDelete'),
    path('switchActiveProject/', views.switchActiveProject, name='switchActiveProject'),
]
