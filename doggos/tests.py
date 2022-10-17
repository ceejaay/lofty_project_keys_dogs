from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.core.files import File
from datetime import timedelta, date
from lofty_app import settings
from PIL import Image, ImageChops
import random
import pyimgur
import sys
import shutil
import os
import tempfile


from doggos.models import DogImage
from doggos.views import DogViewSet
DOG_PIC = "images/test_doggy.jpg"
# Create your tests here.

class DogImageTest(APITestCase):

    def setUp(self):
       self.new_pic = DogImage()
       self.client = APIClient()
       self.dog_view = DogViewSet()
       self.imgur = pyimgur.Imgur(settings.IMGUR_KEY)



    def test_for_saved_photo(self):
        dogs = self.client.get('/dogs/', format='json')
        self.assertEqual(dogs.status_code, 200)
        new_dog = DogImage.objects.last()
        #not sure what to test here


    def test_for_altered_photo(self):
        self.client.get('/dogs/', format="json")
        two_dogs = DogImage.objects.last()
        img1 = two_dogs.url
        img2 = two_dogs.duplicate_url
        print(img1, img2)
        # i = self.imgur.get_image(img1)
        


        # img = img.convert("L")
        # img = img.save("images/dup_doggy.jpg")
        # img1 = Image.open(original)
        # img2 = Image.open("images/dup_doggy.jpg")
        # with self.assertRaises(ValueError):
        #     ImageChops.difference(img1, img2)

    def test_for_uploaded_photo(self):
        pass
