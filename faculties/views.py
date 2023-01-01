from django.shortcuts import render, redirect
from departments.models import Department
from .models import Faculty
from django.http import Http404


# Create your views here.

def faculties(request):
    faculties = Faculty.objects.all()
    dept = Department.objects.all()
    context = {
        'faculties':faculties,
        'dept':dept,
    }
    return render(request, 'faculties-page.html', context)

def details(request, id):
    faculty = Faculty.objects.get(pk=id)
    dept = Department.objects.filter(faculty=faculty)
    context = {
        'dept':dept,
        'faculty':faculty,
    }
    return render(request, 'faculty-details.html', context)

def addFaculty(request):
    return render(request, 'add-faculty.html')

def add(request):
    facultyName = request.POST.get('newFaculty')
    # facultyList = Faculty.objects.all()
    # facultyCheck = True
    if facultyName != '':
        # for f in facultyList:
        #     if f.facultyName==facultyName:
        #         facultyCheck&=False
        #         raise Http404("Faculty already exists")
        #     else:
        newFaculty = Faculty.objects.create(facultyName=facultyName)
        newFaculty.save()
    return redirect('/faculties')

def cancel(request):
    return redirect('/faculties')

def delete(request, id):
    faculty = Faculty.objects.get(pk=id)
    faculty.delete()
    return redirect('/faculties')

def deleteFaculty(request, id):
    faculty = Faculty.objects.get(pk=id)
    context = {'faculty':faculty}
    return render(request, 'delete-faculty.html', context)
    
def cancelDelete(request):
    return redirect('/faculties')

def editFaculty(request, id):
    faculty = Faculty.objects.get(pk=id)
    context ={
        'faculty':faculty
    }
    return render(request, 'edit-faculty.html', context)

def edit(request, id):
    faculty = Faculty.objects.get(pk=id)
    facultyName = request.POST.get('newFaculty')
    if facultyName != '':
        faculty.facultyName = facultyName
        faculty.save()
    return redirect('/faculties')
