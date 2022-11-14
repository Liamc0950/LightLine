from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


app_name = 'database'

urlpatterns = [

    #DATABASE
    path('', views.databaseView, name='database'),
    path('importLWCSV/', views.ImportCSVLWFormView.as_view(), name='importLWCSV'),
    #instrument delete buttons
    path('deleteInstrument/<int:instrumentID>', views.instumentDelete, name='deleteCue'),


]
