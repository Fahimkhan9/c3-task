
from rest_framework import serializers
from .models import pizza



class PizzeSerializer(serializers.ModelSerializer):
    class Meta:
        model = pizza
        fields = '__all__'