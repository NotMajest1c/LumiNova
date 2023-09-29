from rest_framework import serializers
from .models import product

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=('title','description','price')