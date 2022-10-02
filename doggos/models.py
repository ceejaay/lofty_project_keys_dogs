from django.db import models


class DogImage(models.Model):
    img = models.ImageField(upload_to='images')


class DuplicateDog(models.Model):
    img = models.ImageField(upload_to="images")
    original_dog_id = models.ForeignKey(DogImage, on_delete=models.CASCADE)
# Create your models here.
