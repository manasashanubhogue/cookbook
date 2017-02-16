from rest_framework import serializers
from .models import Commands

class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commands
        fields = '__all__'
