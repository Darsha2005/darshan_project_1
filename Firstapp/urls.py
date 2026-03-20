from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcomepage, name="openscript"),
    path("home/<str:name>/",views.homepage,name="homescript"),
    path("main/", views.mainPage,name="mainContent"),
    path("content/",views.contentPage,name="conPage"),
    path("about/<str:name>/<int:age>/",views.aboutPage,name="aboutInfo"),
    path("index/<str:name>/<int:age>/",views.indexPage,name="indexLoad"),

]
