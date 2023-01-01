from django.shortcuts import render, redirect
from .models import Subject_Lecturer
from lecturers.models import Lecturer
from courses.models import Course

# Create your views here.

def subjects(request):
    subjects = Subject_Lecturer.objects.all()
    context = {
        'subjects':subjects,
    }
    s1 = Subject_Lecturer.objects.get(id=1)
    return render(request, 'subjects-page.html', context)

def createSubject(request):
    courses = Course.objects.all()
    lecturers = Lecturer.objects.all()
    context = {
        'courses':courses,
        'lecturers':lecturers,
    }
    return render(request, 'create-subject.html', context)

def create(request):
    courseName = request.POST.get('course')
    courseTitle = courseName[10:]
    course = Course.objects.get(courseTitle=courseTitle)
    lecturerIdList = request.POST.getlist('lecturer')
    newSubject = Subject_Lecturer.objects.create(course=course)
    for i in lecturerIdList:
        lecturer = Lecturer.objects.get(id=i)
        print(lecturer)
        newSubject.lecturer.add
    newSubject.save()
    return redirect('/courses')

def cancel(request):
    return redirect('/subjects')

def deleteSubject(request, id):
    subject = Subject_Lecturer.objects.get(pk=id)
    context = {'subject':subject}
    return render(request, 'delete-subject.html', context)

def delete(request, id):
    subject = Subject_Lecturer.objects.get(pk=id)
    subject.delete()
    return redirect('/subjects')

def cancelDelete(request):
    return redirect('/subjects')