from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_photo_url = models.URLField(default="https://i.imgur.com/up0yEK1.png")

    def __str__(self):
        return self.username


class Notebook(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    creation_date_time = models.DateTimeField(auto_now_add=True)
    last_updated_date_time = models.DateTimeField(auto_now=True)
    favorite = models.BooleanField(default=False)
    notebook = models.ForeignKey(Notebook, related_name="notes", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    notes = models.ManyToManyField(Note, related_name="tags", blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
