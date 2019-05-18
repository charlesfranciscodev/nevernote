from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_photo_url = models.URLField(default="https://i.imgur.com/up0yEK1.png")

