from django.db import models

from django.db import models


class DogImage(models.Model):
    img = models.ImageField(upload_to="images")
    altered_img  = models.ImageField(upload_to="images")

    url = models.CharField(max_length=128, default="none")
    duplicate_url = models.CharField(max_length=128, default='none')

    filename = models.CharField(max_length=128, default="none")
    height = models.IntegerField(default=100)
    width = models.IntegerField(default=100)
    file_type = models.CharField(max_length=32)
# Create your models here.
