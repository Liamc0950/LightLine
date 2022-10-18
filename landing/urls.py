from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    #landing page
    path('', views.index, name="index")
]