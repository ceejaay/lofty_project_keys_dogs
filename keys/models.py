from django.db import models

# Create your models here.


class Key(models.Model):
    key = models.CharField(max_length=64, unique=True, blank=False, error_messages={'invalid': "Resource already exists"})
    value = models.IntegerField(default=0)

