from django.shortcuts import render, redirect
from .models import Level

# Create your views here.
def level(request):
    level = Level.objects.all()
    context = {
        'level':level,
    }
    return render(request, 'level-page.html', context)


def addLevel(request):
    level = Level.objects.all
    context = {
        'level':level,
    }
    return render(request, 'add-level.html', context)

def add(request):
    title = request.POST.get('newLevel')
    if level != '':
        newlevel = Level.objects.create(title=title)
        newlevel.save()
    return redirect('/levels')

def cancelAdd(request):
    return redirect('/levels')

def delete(request, pk):
    level = Level.objects.get(pk=pk)
    level.delete()
    return redirect('/levels')

def deleteLevel(request, pk):
    level = Level.objects.get(pk=pk)
    context = {'level':level}
    return render(request, 'delete-level.html', context)

def cancelDelete(request):
    return redirect('/levels')
