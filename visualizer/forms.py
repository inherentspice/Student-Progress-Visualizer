from django import forms
from visualizer.models import Classroom, Student

class ClassroomInformationForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'

class StudentInformationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
