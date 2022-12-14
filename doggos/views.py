from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from doggos.models import DogImage
from rest_framework import viewsets, permissions
from django.core.files import File
from rest_framework.response import Response
from doggos.serializers import DogSerializer
from django.views import generic
from django.template import loader
from django.conf import settings
import json
import random
import requests
import tempfile
import os
import pyimgur
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from django.core import files
RANDOM = 'https://dog.ceo/api/breeds/image/random'

imgur = pyimgur.Imgur(settings.IMGUR_KEY)
from faker import Faker
fake = Faker()

def dog_preview(request, pk):
    dogs = get_object_or_404(DogImage, pk=pk)
    context = {'dog_preview': [dogs]}
    return render(request, 'doggos/preview.html', context)

class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer

    def get_images(self):
        response = requests.get(RANDOM).json()
        i = requests.get(response['message'], stream=True)
        try:
            if i.status_code == 200:
                temp_file = tempfile.NamedTemporaryFile()
        except:
            return Response({"status": 500, "message": "try againg later"})

        for block in i.iter_content(1024 * 8):
            if not block:
                break
            temp_file.write(block)
        return temp_file



    def alter_images(self, images):
        dup_dog_file = f"images/duplicate_dog{random.randint(0, 1000)}.jpg"
        with Image.open(images.name) as dog_pic:
            dog_pic = dog_pic.convert("L")
            dog_pic = dog_pic.save(dup_dog_file)
        return dup_dog_file


    def get_dog(self, request):
        # get the dog pic 
        temp_file = self.get_images()
        new_dog = DogImage()

        file_name = f"dog_pic_{random.randint(0, 1000)}.jpg"
        dog_name = fake.first_name()
        new_dog.img.save(file_name, File(open(temp_file.name, 'rb')))
        # duplicate and alter the file
        dup_dog_file = self.alter_images(temp_file) 

        # upload dog pics to host

        upload_dog2= imgur.upload_image(dup_dog_file, title=f"B&W_{dog_name}")
        upload_dog1 = imgur.upload_image(temp_file.name, title=dog_name)

        # save new data to the object and save
        new_dog.url = upload_dog1.link
        new_dog.duplicate_url = upload_dog2.link
        new_dog.height = upload_dog2.height
        new_dog.width = upload_dog2.width
        new_dog.file_type = upload_dog2.type
        new_dog.preview_link = f"http://localhost:8000/dogs/preview/{new_dog.id}"
        new_dog.filename=dog_name
        new_dog.save()

        serialized = DogSerializer(new_dog)
        return Response(serialized.data)
# Create your views here.
