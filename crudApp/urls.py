from django.urls import path
from . import views

urlpatterns = [
    path("Employee/", views.employee_list, name='employee_data'),
]
