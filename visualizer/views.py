from http.client import HTTPResponse
from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from .models import Class, Student
from .forms import ClassInformationForm

def index(request):
    class_list = Class.objects.order_by('grade')
    context = {
        'class_list': class_list
    }
    return render(request, 'visualizer/index.html', context)

def class_registration(request):
    if request.method == 'POST':
        form = ClassInformationForm(request.POST)

        if form.is_valid():
            return redirect('classroom-created')
    else:
        form = ClassInformationForm()

    return render(request, 'visualizer/class_registration.html', {'form': form})

def classroom_created(request):
    return render(request, 'visualizer/classroom_created.html')

def class_overview(request, class_id):
    students = get_list_or_404(Student, pk=class_id)
    return render(request, 'visualizer/class_overview.html', {'students': students})

def grades(request, class_name):
    response = 'You\'re looking at the grades for class %s'
    return HttpResponse(response % class_name)
