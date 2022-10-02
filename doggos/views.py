from django.http import HttpResponse
from django.shortcuts import render
from doggos.models import DogImage
from rest_framework import viewsets
from rest_framework import permissions
from doggos.serializers import DogSerializer
import json
import requests
import tempfile
from django.core import files
RANDOM = 'https://dog.ceo/api/breeds/image/random'

class DogViewSet(viewsets.ModelViewSet):
    queryset = DogImage.objects.all()
    serializer_class = DogSerializer

    def get_dog(self, request):
        response = requests.get(RANDOM).json()
        dog_url = response['message']

        i = requests.get(dog_url, stream=True)
        if i.status_code == 200:
            temp_file = tempfile.NamedTemporaryFile()
        for block in i.iter_content(1024 * 8):
            if not block:
                break
            temp_file.write(block)

        dog_img = DogImage()
        dog_img.img.save("new dog", files.File(temp_file))


        return HttpResponse()


# Create your views here
