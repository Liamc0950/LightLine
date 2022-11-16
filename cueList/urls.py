from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'cueList'

urlpatterns = [

    #ROOT
    path('', views.cueListView, name='cueList'),

    #cueList app live update
    path('updateCue/', views.updateCue, name='updateCue'),
    #cueList Selection
    path('switchActiveCueList/', views.switchActiveCueList, name='switchActiveCueLis'),
    #cueList delete buttons
    path('deleteCue/<int:cueID>', views.cueDeleteCueList, name='deleteCue'),
    #delete cueList
    path('deleteCueList/<int:cueListID>', views.cueListDeleteDashboard, name='deleteCueList'),
    #cueList add cue
    path('addCue/', views.CueCreateView.as_view(), name='addCue'),
    path('addNextCue/<int:lastCueID>', views.cueCreateNextCueList, name='addNextCue'),
    #cueList add Header
    path('addHeader/', views.HeaderCreateView.as_view(), name='addHeader'),
    #CueList Print Layout
    path('printLayout/', views.printLayout, name='printLayout'),
    #CueList Print
    path('print/', views.print, name='print'),
    #CueList Export Eos CSV
    path('exportEosCSV/<int:activeCueListID>', views.exportEosCSV, name='exportEosCSV'),
    #CueList Create CueList
    path('createCueList', views.CueListCreateView.as_view(), name='createCueList'),

]
