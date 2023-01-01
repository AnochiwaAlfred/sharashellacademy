from django.shortcuts import render, redirect
from .models import Lecturer
from faculties.models import Faculty
from departments.models import Department
from bridge.models import Subject_Lecturer

# Create your views here.

def lecturer(request):
    lecturer = Lecturer.objects.all()
    context = {
        'lecturer':lecturer,
    }
    return render(request, 'lecturer-page.html', context)

def createLecturer(request):
    faculty = Faculty.objects.all
    department = Department.objects.all()

    context = {
        'faculty':faculty,
        'department':department,
    }
    return render(request, 'create-lecturer.html', context)

def create(request):
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    idNumber = request.POST.get('idNumber')
    dateOfBirth = request.POST.get('dateOfBirth')
    title = request.POST.get('title')
    gender = request.POST.get('gender')
    rank = request.POST.get('rank')
    phone = str(request.POST.get('phone')).replace(' ', '')
    email = request.POST.get('email')
    address = request.POST.get('address')
    yearOfAppointment = request.POST.get('yearOfAppointment')
    departmentName = request.POST.get('department')
    facultyName = request.POST.get('faculty')
    department = Department.objects.get(departmentName=str(departmentName).replace('Department of ', ''))
    faculty = Faculty.objects.get(facultyName=str(facultyName).replace('Faculty of ', ''))
    firstNameLower = str(firstName).lower()
    lastNameLower = str(lastName).lower()
    username = f'{firstNameLower}{lastNameLower}@sharashellacademy.com'

    # lecturerList = Lecturer.objects.all()
    # lecturerCheck = True
    # for i in lecturerList:
    #     if i.idNumber==idNumber:
    #         lecturerCheck&=False
    #     else:
    #         if i.username==username:
    #             lecturerCheck&=False
    #         else:
    # print(firstName, lastName, idNumber, dateOfBirth, title, gender, rank, phone, email, address, department, faculty, yearOfAppointment, username)
    newLecturer = Lecturer.objects.create(firstName=firstName, lastName=lastName, idNumber=idNumber, dateOfBirth=dateOfBirth, title=title, gender=gender, rank=rank, phone=phone, email=email, address=address, department=department, faculty=faculty, yearOfAppointment=yearOfAppointment, username=username)
    newLecturer.save()
    return redirect('/lecturers')

def cancel(request):
    return redirect('/lecturers')

def deleteLecturer(request, id):
    lecturer = Lecturer.objects.get(pk=id)
    context = {'lecturer':lecturer}
    return render(request, 'delete-lecturer.html', context)

def delete(request, id):
    lecturer = Lecturer.objects.get(pk=id)
    lecturer.delete()
    return redirect('/lecturers')

def cancelDelete(request):
    return redirect('/lecturers')

def profile(request, id):
    lecturer = Lecturer.objects.get(pk=id)
    subject = Subject_Lecturer.objects.filter(lecturer=lecturer)
    context = {
        'lecturer':lecturer,
        # 'subject':subject,
    }
    return render(request, 'lecturer-profile.html', context)

def editLecturer(request, id):
    lecturer = Lecturer.objects.get(pk=id)
    faculty = Faculty.objects.all
    department = Department.objects.all()

    context = {
        'faculty':faculty,
        'department':department,
        'lecturer':lecturer,
    }
    return render(request, 'edit-lecturer.html', context)


def edit(request, id):
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    title = request.POST.get('title')
    rank = request.POST.get('rank')
    phone = str(request.POST.get('phone')).replace(' ', '')
    email = request.POST.get('email')
    address = request.POST.get('address')
    firstNameLower = str(firstName).lower()
    lastNameLower = str(lastName).lower()
    username = f'{firstNameLower}{lastNameLower}@sharashellacademy.com'
    lecturer = Lecturer.objects.get(pk=id)

    lecturer.firstName=firstName
    lecturer.lastName=lastName
    lecturer.title=title
    lecturer.rank=rank
    lecturer.phone=phone
    lecturer.email=email
    lecturer.address=address
    lecturer.username=username

    lecturer.save()

    return redirect('/lecturers')