from django.shortcuts import render, redirect, get_list_or_404
from django.http import JsonResponse
from .models import Classroom, Student, Grades
from .forms import ClassroomInformationForm, StudentInformationForm, GradesInformationForm
from django.urls import reverse

def home_view(request, *args, **kwargs):
    return render(request, 'visualizer/home.html')

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

def classroom_update(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)

    if request.method == 'POST':
        form = ClassroomInformationForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            return redirect('visualizer:classroom', classroom.id)

    else:
        form = ClassroomInformationForm(instance=classroom)

    return render(request, 'visualizer/classroom_update.html',
                  {'classroom': classroom, 'form': form})

def student_update(request, classroom_id, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        form = StudentInformationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('visualizer:classroom', classroom_id)

    else:
        form = StudentInformationForm(instance=student)

    return render(request, 'visualizer/student_update.html',
                  {'form': form})


def classroom_overview(request, classroom_id):
    if request.method == 'POST':
        form = StudentInformationForm(request.POST, )

        if form.is_valid():
            student = form.save()
            student_class = Student.objects.filter(classroom_name=classroom_id)
            return render(request, 'visualizer/classroom_overview.html',
                          {'student_class': student_class, 'form': form})
    else:
        form = StudentInformationForm()

        try:
            student_class = Student.objects.filter(classroom_name=classroom_id)

        except Student.DoesNotExist:
            return render(request, 'visualizer/classroom_overview.html',
                          {'form': form})

    return render(request, 'visualizer/classroom_overview.html',
                  {'student_class': student_class, 'form': form})

def classroom_delete(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    if request.method == 'POST':
        classroom.delete()
        return redirect('visualizer:index')

    return render(request, 'visualizer/classroom_delete.html',
                  {'classroom': classroom})

def student_delete(request, classroom_id, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('visualizer:classroom', classroom_id)

    return render(request, 'visualizer/student_delete.html',
                  {'student': student})

def grades(request, classroom_id, student_id):
    grades = Grades.objects.filter(student_name=student_id)
    if request.method == 'POST':

        form = GradesInformationForm(request.POST)

        if form.is_valid():
            grades = form.save()
            return redirect('visualizer:classroom', classroom_id)
    else:
        form = GradesInformationForm()

    return render(request, 'visualizer/student_performance.html',
                  {'grades': grades, 'form': form})


def charts(request, classroom_id, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'visualizer/charts.html', {'student': student})


def grades_chart(request, student_id):
    labels = []
    data = []

    queryset = Grades.objects.filter(student_name=student_id)
    for subject in queryset:
        labels.append(subject.subject)
        data.append(subject.grades)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
