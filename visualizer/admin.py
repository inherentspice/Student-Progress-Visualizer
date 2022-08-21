from django.contrib import admin

from .models import Classroom, Student, Grades

admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Grades)
