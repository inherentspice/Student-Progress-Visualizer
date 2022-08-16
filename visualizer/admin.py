from django.contrib import admin

from .models import Class, Student, Grades

admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Grades)
