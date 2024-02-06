from django.db import models

# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(max_length = 63)


class Teacher(models.Model):
    teachers_name = models.CharField(max_length = 63)
    teachers_surname = models.CharField(max_length = 63)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE, null = True)


class Class(models.Model):
    class_name = models.CharField(max_length = 63)


class Student(models.Model):
    students_name = models.CharField(max_length = 63)
    students_surname = models.CharField(max_length = 63)
    classes = models.ForeignKey(Class, on_delete = models.CASCADE, null = True)