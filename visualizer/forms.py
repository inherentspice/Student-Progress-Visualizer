from django import forms

class ClassInformationForm(forms.Form):
    class_name = forms.CharField(max_length=200)
    grade = forms.CharField(max_length=40)
