from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


app_name = 'script'

urlpatterns = [

    #SCRIPT
    path('', views.scriptView, name='script'),
    path('importScript/', views.ScriptUploadView, name='importScriptPDF'),

]
