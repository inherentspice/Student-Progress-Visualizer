from django import forms

class ClassroomInformationForm(forms.Form):
    classroom_name = forms.CharField(max_length=200)
    grade = forms.CharField(max_length=40)
