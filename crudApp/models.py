from django.db import models

# Create your models here.

class StudentModel(models.Model):
    EmployeeId = models.IntegerField()
    EmployeeName = models.CharField(max_length=200)
    Designation = models.CharField(max_length=150)
    gender = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)

    def __str__(self):
        return self.EmployeeName