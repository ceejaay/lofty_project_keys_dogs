from django.http import HttpResponse
from django.shortcuts import render
from doggos.models import DogImage
from rest_framework import viewsets, permissions
from doggos.serializers import DogSerializer
from django.views import generic
from django.template import loader
import json
import random
import requests
import tempfile
import os
import pyimgur
from django.core import files
RANDOM = 'https://dog.ceo/api/breeds/image/random'

imgur = pyimgur.Imgur("4f472bc818f1daf")

def dog_preview(request, pk):
    dogs = DogImage.objects.get(pk=pk)
    context = {'dog_preview': [dogs]}
    # print(context)
    return render(request, 'doggos/preview.html', context)

class DogViewSet(viewsets.ModelViewSet):
    queryset = DogImage.objects.all()
    serializer_class = DogSerializer

    def get_dog(self, request):
        response = requests.get(RANDOM).json()
        dog_url = response['message']

        i = requests.get(dog_url, stream=True)
        if i.status_code == 200:
            temp_file = tempfile.NamedTemporaryFile()
            print(vars(temp_file))
        for block in i.iter_content(1024 * 8):
            if not block:
                break
            temp_file.write(block)

        uploaded_dog = imgur.upload_image(temp_file.name)
        print(uploaded_dog.link)
        dog_img = DogImage()
        file_name = f"new_dog{random.randint(0, 10000)}.jpg"
        dog_img.img.save(file_name,  files.File(temp_file))
        dog_img.url = uploaded_dog.link 
        dog_img.save()

        return HttpResponse(dog_img.id)



