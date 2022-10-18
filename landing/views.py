from django.shortcuts import render


def index(request):
    #Landing Page
    return render(request, 'index.html')
