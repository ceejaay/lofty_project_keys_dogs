from django.test import TestCase
from django.core.files import File
from datetime import timedelta, date
import sys
from doggos.models import DogImage
DOG_PIC = "images/test_dog.jpg"
# Create your tests here.

class DogImageTest(TestCase):

    def setUp(self):
       self. new_pic = DogImage()


    def test_for_saved_photo(self):
        self.new_pic.img.save("test_doggy.jpg", File(open(DOG_PIC, 'rb')))
        dog_from_db = DogImage.objects.last()
        self.new_pic.height = 100
        self.new_pic.width = 200
        self.assertEqual('images/test_doggy.jpg', dog_from_db.img)

    def test_for_altered_photo(self):
        pass

    def test_for_uploaded_photo(self):
        pass
