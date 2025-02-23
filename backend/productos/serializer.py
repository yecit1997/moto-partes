from rest_framework import serializers
from .models import Productos

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        field = '__all__'