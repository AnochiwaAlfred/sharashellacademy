from django.shortcuts import render, redirect
from .models import Department
from faculties.models import Faculty
from students.models import Student
from django.http import Http404

# Create your views here.
def department(request):
    dept = Department.objects.all()
    context = {
        'dept':dept,
    }
    return render(request, 'dept-page.html', context)

def addDepartment(request):
    faculty = Faculty.objects.all()
    context = {
        'faculty':faculty,
    }
    return render(request, 'add-department.html', context)

def add(request):
    departmentName = request.POST.get('newDepartment')
    facultyName = request.POST.get('faculty')
    faculty = Faculty.objects.get(facultyName=str(facultyName).replace('Faculty of ', ''))
    courseDurationText = request.POST.get('courseDuration')
    courseDuration = str(courseDurationText).replace(' Years', '')
    # departmentList = Department.objects.all()
    # departmentCheck = True
    if departmentName != '':
        # for d in departmentList:
        #     if d.departmentName==departmentName:
        #         departmentCheck&=False
        #         raise Http404("Department already exists")
        #     else:
        newDepartment = Department.objects.create(departmentName=departmentName, courseDuration=courseDuration, faculty=faculty)
        newDepartment.save()
    return redirect('/departments')

def cancel(request):
    return redirect('/departments')

def delete(request, id):
    department = Department.objects.get(pk=id)
    department.delete()
    return redirect('/departments')

def deleteDepartment(request, id):
    department = Department.objects.get(pk=id)
    context = {'department':department}
    return render(request, 'delete-department.html', context)

def cancelDelete(request):
    return redirect('/departments')

def details(request, id):
    department = Department.objects.get(pk=id)
    student = Student.objects.filter(department=department)
    context = {
        'department':department,
        'student':student,
    }
    return render(request, 'department-details.html', context)

def editDepartment(request, id):
    department = Department.objects.get(pk=id)
    faculty = Faculty.objects.all()
    context = {
        'department':department,
        'faculty':faculty,
    }
    return render(request, 'edit-department.html', context)

def edit(request, id):
    departmentName = request.POST.get('newDepartment')
    facultyName = request.POST.get('faculty')
    faculty = Faculty.objects.get(facultyName=str(facultyName).replace('Faculty of ', ''))
    courseDurationText = request.POST.get('courseDuration')
    courseDuration = str(courseDurationText).replace(' Years', '')
    department = Department.objects.get(pk=id)
    if departmentName != '':
        department.departmentName = departmentName
        department.faculty = faculty
        department.courseDuration =courseDuration
        department.save()
    return redirect('/departments')