from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Classroom(models.Model):
    classroom_name = models.CharField(max_length=200)
    grade = models.CharField(max_length=40)

    def __str__(self):
        return self.class_name + '(' + self.grade + ')'

class Student(models.Model):
    student_name = models.CharField(max_length=200)
    student_classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name

class Grades(models.Model):
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Subjects(models.TextChoices):
        sight_words = "Sight Words"
        reading = "Reading"
        math = "Math"
        writing = "Writing"
        phonics = "Phonics"

    subject = models.CharField(
        max_length=12,
        choices=Subjects.choices,
        default=Subjects.reading,
        )
    grades = models.PositiveIntegerField(default=50, validators=[MinValueValidator(0), MaxValueValidator(100)])
