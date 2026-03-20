from django.db import models

# Create your models here.

class StudentModel(models.Model):
    studentName = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)
    department = models.CharField(max_length=200)

    def __str__(self):
        return self.studentName
