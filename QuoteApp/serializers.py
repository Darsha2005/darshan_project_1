from rest_framework import serializers
from .models import AuthorModel, QuoteModel


class authorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = "__all__"


class quoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteModel
        fields = "__all__"