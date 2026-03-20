from django.urls import path
from . import views

urlpatterns = [
    path("patient/", views.MedicalListCreate.as_view(), name="patient-list"),
    path("patient/<int:pk>/", views.MedicalDetail.as_view(), name="patient-detail"),

]