from django.test import TestCase
from django.core.files import File
from datetime import timedelta, date
from PIL import Image, ImageChops
import random
import sys
import shutil
import os
import tempfile
from doggos.models import DogImage
from doggos.views import DogViewSet as dogView
DOG_PIC = "images/test_doggy.jpg"
# Create your tests here.

class DogImageTest(TestCase):

    def setUp(self):
       self.new_pic = DogImage()


    def test_for_saved_photo(self):
        new_dog_pic = f"saved_doggy{random.randint(0, 1000)}"
        self.new_pic.img.save(new_dog_pic, File(open(DOG_PIC, 'rb')))
        dog_from_db = DogImage.objects.last()
        self.new_pic.height = 100
        self.new_pic.width = 100
        self.assertEqual("images/" + new_dog_pic, dog_from_db.img)
        if os.path.isfile("images/" + new_dog_pic):
            os.remove("images/" + new_dog_pic)
        self.new_pic.save()
        self.assertEqual(dog_from_db.height, 100)
        self.assertEqual(dog_from_db.width, 100)




    def test_for_altered_photo(self):
        pass
        # temp_file = dogView.get_images()



            # altered_image = dogView.alter_images(img)
            # print(altered_image)
            # img = img.convert("L")
            # img = img.save("images/dup_doggy.jpg")
        # img1 = Image.open(original)
        # img2 = Image.open("images/dup_doggy.jpg")
        # with self.assertRaises(ValueError):
        #     ImageChops.difference(img1, img2)

    def test_for_uploaded_photo(self):
        pass
