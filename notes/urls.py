from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [

    #NOTES
    path('', views.notes, name='notes'),
    path('createWorkNote/', views.createWorkNote, name='createWorkNote'),
    #Work Note live update
    path('updateWorkNote/', views.updateWorkNote, name='updateWorkNote'),
    path('completeNote/<int:noteID>', views.completeNote, name='completeNote'),
]
