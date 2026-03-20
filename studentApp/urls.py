from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.studentView,name="data"),
    path("students/<int:id>/",views.studentUpdateView,name="updateView"),
    path("studentValue/", views.studentDataView.as_view(),name="studentapi"),
    path("studentValue/<int:pk>/", views.studentDataModifyView.as_view(), name="studentApiName"),
]