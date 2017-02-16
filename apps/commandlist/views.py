from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CommandSerializer
from .models import Command

class CommandViewSet(ModelViewSet):
    serializer_class = CommandSerializer

    def get_query_set(self):
        return Command.objects.filter(self.request.user)
