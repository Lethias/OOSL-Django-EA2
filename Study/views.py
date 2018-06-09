from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from Study.models import *
from Study.forms import *


def get_student_list(request):
    students = Student.objects.all().order_by('lastname')

    return render(request, 'students.html', {'page_title': 'Studenten', 'students': students})


def get_module_list(request):
    module = Modul.objects.all().order_by('modulname')

    return render(request, 'module.html', {'page_title': 'Module', 'module': module})


def get_studiengang_list(request):
    studiengaenge = Studiengang.objects.all().order_by('studiengangname')

    return render(request, 'studiengang.html', {'page_title': 'Studiengänge', 'studiengaenge': studiengaenge})


def manipulate_student(request, pk=None):
    if pk == None:
        student = Student()
        page_title = 'Neuen Studenten erstellen'
    else:
        student = get_object_or_404(Student, pk=pk)
        page_title = 'Studenten editieren'

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Erfolgreich erstellt')
            return HttpResponseRedirect(reverse('showStudent'))
        else:
            messages.error(request, 'Fehler bitte korrigieren')
    else:
        form = StudentForm(instance=student)

    return render(request, 'manstudent.html', {'page_title': page_title, 'form': form})
