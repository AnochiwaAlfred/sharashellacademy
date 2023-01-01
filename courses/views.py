from django.shortcuts import render, redirect
from .models import Course
from students.models import Student
from departments.models import Department
from faculties.models import Faculty
from levels.models import Level

# Create your views here.
def courses(request):
    courses = Course.objects.all()
    students= Student.objects.all()
    # for s in studentList:
        # if ns.courseTitle in s.courses:

    context = {
        'courses':courses,
        'students':students,
    }
    return render(request, 'courses-page.html', context)

def createCourse(request):
    departments = Department.objects.all()
    faculties = Faculty.objects.all()
    levels = Level.objects.all()
    context = {
        'departments':departments,
        'faculties':faculties,
        'levels':levels,
    }
    return render(request, 'create-course.html', context)

def create(request):
    courseCode = request.POST.get('courseCode')
    courseTitle = request.POST.get('courseTitle')
    creditLoad = request.POST.get('creditLoad')
    departmentName = request.POST.get('department')
    department = Department.objects.get(departmentName=str(departmentName).replace('Department of ', ''))
    facultyName = request.POST.get('faculty')
    faculty = Faculty.objects.get(facultyName=str(facultyName).replace('Faculty of ', ''))
    levelName = request.POST.get('level')
    level = Level.objects.get(title=levelName)
    if courseCode != '':
        if courseTitle != '':
            newCourse = Course.objects.create(courseCode=courseCode, courseTitle=courseTitle, creditLoad=creditLoad, department=department, faculty=faculty, level=level)
            newCourse.save()
    return redirect('/courses')

def cancel(request):
    return redirect('/courses')

def deleteCourse(request, id):
    course = Course.objects.get(pk=id)
    context = {'course':course}
    return render(request, 'delete-course.html', context)

def delete(request, id):
    course = Course.objects.get(pk=id)
    course.delete()
    return redirect('/courses')

def cancelDelete(request):
    return redirect('/courses')

def details(request, id):
    course = Course.objects.get(pk=id)
    context = {
        'course':course,
    }
    return render(request, 'course-details.html', context)

def editCourse(request, id):
    course = Course.objects.get(pk=id)
    departments = Department.objects.all()
    faculties = Faculty.objects.all()
    levels = Level.objects.all()
    context = {
        'departments':departments,
        'faculties':faculties,
        'levels':levels,
        'course':course
    }
    return render(request, 'edit-course.html', context)

def edit(request, id):
    editCourse = Course.objects.get(pk=id)
    courseCode = request.POST.get('courseCode')
    courseTitle = request.POST.get('courseTitle')
    creditLoad = request.POST.get('creditLoad')
    departmentName = request.POST.get('department')
    department = Department.objects.get(departmentName=str(departmentName).replace('Department of ', ''))
    facultyName = request.POST.get('faculty')
    faculty = Faculty.objects.get(facultyName=str(facultyName).replace('Faculty of ', ''))
    levelName = request.POST.get('level')
    level = Level.objects.get(title=levelName)
    if courseCode != '':
        if courseTitle != '':
            editCourse.courseCode = courseCode
            editCourse.courseTitle = courseTitle
            editCourse.department = department
            editCourse.faculty = faculty
            editCourse.creditLoad = creditLoad
            editCourse.save()
           
    return redirect('/courses')