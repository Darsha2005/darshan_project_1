from django.shortcuts import render
from .models import StudentModel

def employee_list(request):
    employees = StudentModel.objects.filter(Designation="Manager")
    return render(request, "crudApp/employee_list.html", {"employees": employees})
