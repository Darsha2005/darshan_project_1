from rest_framework import serializers
from .models import MedicalInfo


class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInfo
        fields = "__all__"