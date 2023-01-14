from email.policy import default
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User (AbstractUser):
    phone = models.CharField(max_length = 13)
    email = models.EmailField(max_length=254, unique= True)
    is_verified = models.BooleanField(default = False)


