from django.urls import path
from .import tViews
from . import views

urlpatterns = [
    path("Table/",tViews.medicalInfo ,name="registration"),
    path("updateDataForm/<int:id>/", tViews.updateMedicalInfo,name="updateData"),
    path("deleteDataForm/<int:id>/", tViews.deleteMedicalInfo,name="deleteData"),
]