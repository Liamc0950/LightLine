from django.urls import path
from . import views

app_name = 'dashboard'


urlpatterns = [
    #dashboard page
    path('', views.index, name="index")
]