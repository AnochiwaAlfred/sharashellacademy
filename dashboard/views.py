from django.shortcuts import render
from django.http import HttpResponse
from departments.models import Department

# Create your views here.
def dashb(request):
    return render(request, 'dashboard/dashb.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def base(request):
    dept = Department.objects.all()
    context = {
        'dept':dept
    }
    return render(request, 'dashboard/new-dash.html', context)

def index(request):
    return render(request, 'dashboard/index.html')

