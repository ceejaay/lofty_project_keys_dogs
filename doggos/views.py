from django.http import HttpResponse
from django.shortcuts import render
from doggos.models import DogImage
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from doggos.serializers import DogSerializer
from django.views import generic
from django.template import loader
import json
import random
import requests
import tempfile
import os
import pyimgur
from PIL import Image
from django.core import files
RANDOM = 'https://dog.ceo/api/breeds/image/random'

imgur = pyimgur.Imgur("4f472bc818f1daf")

def dog_preview(request, pk):
    dogs = DogImage.objects.get(pk=pk)
    context = {'dog_preview': [dogs]}
    #here we need to get the alterd image link and data.
    # print(context)
    return render(request, 'doggos/preview.html', context)

class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer
    new_dog = DogImage()

    def get_dog(self, request):
        response = requests.get(RANDOM).json()
        dog_url = response['message']

        i = requests.get(dog_url, stream=True)
        if i.status_code == 200:
            temp_file = tempfile.NamedTemporaryFile()
            temp_file2 = tempfile.NamedTemporaryFile()



        for block in i.iter_content(1024 * 8):
            if not block:
                break
            temp_file.write(block)
            temp_file2.write(block)

        upload_dog1 = imgur.upload_image(temp_file.name)
        upload_dog2 = imgur.upload_image(temp_file2.name)
        new_dog = DogImage.objects.create(url=upload_dog1.link, duplicate_url=upload_dog2.link)
        serialized = DogSerializer(new_dog)
        return Response(serialized.data)









