from django.shortcuts import render, redirect
from departments.models import Department
from faculties.models import Faculty
from levels.models import Level
from .models import Student

# Create your views here.

def studentsPage(request):
    students = Student.objects.all()
    context = {
        'students':students
    }
    return render(request, 'students-page.html', context)

def addStudent(request):
    level = Level.objects.all
    faculty = Faculty.objects.all
    department = Department.objects.all
    context = {
        'level':level,
        'faculty':faculty,
        'department':department,
    }
    return render(request, 'add-student.html', context)

def add(request):
    firstName = request.POST['firstname']
    lastName = request.POST['lastname']
    address = request.POST['address']
    phone = request.POST['phone']
    title = request.POST['title']
    regNumber = request.POST['regNumber']
    gender = request.POST['gender']
    yearOfEntry = request.POST['yearOfEntry']
    yearOfGraduation = request.POST['yearOfGraduation']
    department = request.POST['department']
    faculty = request.POST['faculty']
    email = request.POST['email']
    dateOfBirth = request.POST['dateOfBirth']
    firstNameL = str(firstName).lower()
    lastNameL = str(lastName).lower()
    username = f'{firstNameL}{lastNameL}@sharashellacademy.com'
    
    newStudent = Student.objects.create(
        firstName=firstName,
        lastName=lastName,
        address=address,
        phone=phone,
        title=title,
        regNumber=regNumber,
        gender=gender,
        yearOfEntry=yearOfEntry,
        yearOfGraduation=yearOfGraduation,
        department=department,
        faculty=faculty,
        email=email,
        dateOfBirth=dateOfBirth,
        username=username
    )
    newStudent.save()
    return render(request, 'students-page.html')

def cancel(request):
    return redirect('/students')

def studentProfile(request):
    context = {}
    return render(request, 'students-page.html', context)

def deleteStudent(request):
    context = {}
    return render(request, 'students-page.html', context)