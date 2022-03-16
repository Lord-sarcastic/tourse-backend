from django.contrib.auth.models import AbstractUser
from django.db import models

from backend.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
