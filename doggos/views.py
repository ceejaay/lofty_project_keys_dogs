from django.http import HttpResponse
from django.shortcuts import render
from doggos.models import DogImage
from rest_framework import viewsets
from rest_framework import permissions
from doggos.serializers import DogSerializer

class DogViewSet(viewsets.ModelViewSet):
    queryset = DogImage.objects.all()
    serializer_class = DogSerializer

    def get_dog(self, request):
        return HttpResponse("hello doggy")


# Create your views here
