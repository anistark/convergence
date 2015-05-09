from django.db import models

# Create your models here.

from mongoengine import *
from convergence.settings import DBNAME

connect(DBNAME)


class Post(Document):
    title = StringField(max_length=120, required=True)
    title_image = URLField()
    post_url = StringField(required=True)
    author = StringField(max_length=120, required=True)
    content = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)
