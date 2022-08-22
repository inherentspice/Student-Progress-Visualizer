from django import forms
from visualizer.models import Classroom

class ClassroomInformationForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'
