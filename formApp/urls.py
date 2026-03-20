from django.urls import path
from . import views

urlpatterns = [
    path("Biodata/", views.sales, name="Biodata"),
    path("Biodata_output/", views.sales_output, name="Biodata_output"),
]