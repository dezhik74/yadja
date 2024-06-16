from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.utils import timezone


class Photo(models.Model):
    image = models.ImageField(upload_to='photo/')
    created = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=50)
