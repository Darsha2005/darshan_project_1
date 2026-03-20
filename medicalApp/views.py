from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import MedicalInfo
from .serializers import MedicalSerializer


# GET all patients and POST new patient
class MedicalListCreate(ListCreateAPIView):
    queryset = MedicalInfo.objects.all()
    serializer_class = MedicalSerializer


# GET single, PUT update, DELETE patient
class MedicalDetail(RetrieveUpdateDestroyAPIView):
    queryset = MedicalInfo.objects.all()
    serializer_class = MedicalSerializer

