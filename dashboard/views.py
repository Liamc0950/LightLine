from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    #Dashboard Page
    return render(request, 'dashboard/dashboard.html')
