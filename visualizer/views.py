from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from .models import Classroom, Student
from .forms import ClassroomInformationForm, StudentInformationForm
from django.urls import reverse

def index(request):
    classroom_list = Classroom.objects.order_by('grade')
    context = {
        'classroom_list': classroom_list
    }
    return render(request, 'visualizer/index.html', context)

def classroom_registration(request):
    if request.method == 'POST':
        form = ClassroomInformationForm(request.POST)

        if form.is_valid():
            classroom = form.save()
            return redirect(reverse('visualizer:classroom', args=(classroom.id,)))
    else:
        form = ClassroomInformationForm()

    return render(request, 'visualizer/classroom_registration.html', {'form': form})


def classroom_overview(request, classroom_id):
    if request.method == 'POST':
        form = StudentInformationForm(request.POST)

        if form.is_valid():
            student = form.save()
            classroom = Classroom.objects.get(pk=classroom_id)
            student_class = get_list_or_404(Student, classroom_name = classroom_id)
            return render(request, 'visualizer/classroom_overview.html',
                          {'student_class': student_class, 'form': form})
    else:
        form = StudentInformationForm()

    classroom = Classroom.objects.get(pk=classroom_id)
    student_class = get_list_or_404(Student, classroom_name=classroom_id)
    return render(request, 'visualizer/classroom_overview.html',
                  {'student_class': student_class, 'form': form})

def grades(request, class_name):
    response = 'You\'re looking at the grades for class %s'
    return HttpResponse(response % class_name)
