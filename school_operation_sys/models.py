from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(max_length = 63)

    def __str__(self):
        return self.subject_name


class Teacher(models.Model):
    teachers_name = models.CharField(max_length = 63)
    teachers_surname = models.CharField(max_length = 63)
    # subject = models.ForeignKey(Subject, on_delete = models.CASCADE, null = True)

    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.teachers_name


class Class(models.Model):
    class_name = models.CharField(max_length = 63)

    def __str__(self):
        return self.class_name


class Student(models.Model):
    students_name = models.CharField(max_length = 63)
    students_surname = models.CharField(max_length = 63)
    # classes = models.ForeignKey(Class, on_delete = models.CASCADE, null = True)

    classes = models.ManyToManyField(Class)

    def __str__(self):
        return self.students_name


class Schedule(models.Model):
    date = models.DateField(auto_now_add = True)

    subjects = models.ForeignKey(Subject, on_delete = models.DO_NOTHING, related_name = "schedule")
    clas = models.ForeignKey(Class, on_delete = models.DO_NOTHING, related_name = "schedule")
    teacher = models.ForeignKey(Teacher, on_delete = models.DO_NOTHING, related_name = "schedule")

    def __str__(self):
        return f"{self.date}, {self.subjects}, {self.clas}, {self.teacher}"
    

class Grade(models.Model):
    grade = models.IntegerField(validators = [MaxValueValidator(12), MinValueValidator(1)])

    student = models.ForeignKey(Student, on_delete = models.DO_NOTHING, related_name = "grade")
    schedule = models.ForeignKey(Schedule, on_delete = models.DO_NOTHING, related_name = "schedule")

    def __str__(self):
        return f"{self.grade, self.student, self.schedule}"