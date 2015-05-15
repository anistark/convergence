from django.db import models

# Create your models here.

from mongoengine import *


class Post(models.Model):
    title = models.CharField(max_length=120)
    title_image = models.ImageField(upload_to='images/%Y/%m/%d')
    post_url = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    added_by = models.CharField(max_length=32)
    content = models.CharField(max_length=500)
    last_update = models.DateTimeField()


class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=16)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    signuptime = models.DateTimeField()

