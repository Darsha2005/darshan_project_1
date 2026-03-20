from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.indexContent, name='index'),
    path('about-page/', views.aboutContent, name='about'),
]
