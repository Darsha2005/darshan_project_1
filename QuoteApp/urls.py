from django.urls import path
from . import views

urlpatterns = [
    path("author/", views.authorApi.as_view()),
    path("quotes/", views.quoteApi.as_view())
]
