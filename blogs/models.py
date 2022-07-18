from django.db import models
from django.contrib.auth.models import auth, User
# Create your models here.

class Blogs(models.Model):
    image = models.ImageField(upload_to='blogpics')
    title = models.CharField(max_length=100, blank=True)
    desc = models.TextField(blank=True)