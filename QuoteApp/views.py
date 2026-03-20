from django.shortcuts import render
from .models import AuthorModel, QuoteModel
from .serializers import authorSerializer, quoteSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class authorApi(generics.ListCreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = authorSerializer


class quoteApi(generics.ListCreateAPIView):
    queryset = QuoteModel.objects.all()
    serializer_class = quoteSerializer