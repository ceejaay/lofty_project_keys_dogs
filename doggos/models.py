from django.db import models


class DogImage(models.Model):
    img = models.ImageField(upload_to='images')
    url = models.CharField(max_length=128, default="none")
    filename = models.CharField(max_length=128, default="none")
    height = models.IntegerField(default=100)
    width = models.IntegerField(default=100)
    file_type = models.CharField(max_length=32)

class DuplicateDog(models.Model):
    img = models.ImageField(upload_to="images")
    original_dog_id = models.ForeignKey(DogImage, on_delete=models.CASCADE)
    url = models.CharField(max_length=128, default="nond")
    filename = models.CharField(max_length=128)
    height = models.IntegerField(default=100)
    width = models.IntegerField(default=100)
    file_type = models.CharField(max_length=32, default="none")
# Create your models here.
