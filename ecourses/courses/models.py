from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='/uploads/%Y/%m')

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

class Course(models.Model):
    subject = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)