from django.db import models


class DogImage(models.Model):
    img = models.ImageField(upload_to='images')

# Create your models here.
