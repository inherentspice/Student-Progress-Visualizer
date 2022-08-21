from http.client import HTTPResponse
from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from .models import Classroom, Student
from .forms import ClassroomInformationForm

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
            return redirect('classroom-created')
    else:
        form = ClassroomInformationForm()

    return render(request, 'visualizer/classroom_registration.html', {'form': form})

def classroom_created(request):
    return render(request, 'visualizer/classroom_created.html')

def classroom_overview(request, class_id):
    students = get_list_or_404(Student, pk=class_id)
    return render(request, 'visualizer/classroom_overview.html', {'students': students})

def grades(request, class_name):
    response = 'You\'re looking at the grades for class %s'
    return HttpResponse(response % class_name)
