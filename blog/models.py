from django.db import models

# Create your models here.

from mongoengine import *

class Post(models.Model):
    title = models.CharField(max_length=120)
    title_image = models.ImageField(upload_to='images/%Y/%m/%d')
    post_url = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    content = models.CharField(max_length=500)
    last_update = models.DateTimeField()
