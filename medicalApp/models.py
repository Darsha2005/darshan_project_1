from django.db import models

class MedicalInfo(models.Model):
    patientName = models.CharField(max_length=150)
    Age = models.IntegerField()
    disease = models.CharField(max_length=100)
    block = models.CharField(max_length=100)

    def __str__(self):
        return self.patientName