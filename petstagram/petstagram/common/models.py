from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from petstagram.pets.models import Pet

UserModel = get_user_model()


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
