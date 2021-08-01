from django.contrib.auth import get_user_model
from django.db import models

from YouTravel.trips.models import Trip

UserModel = get_user_model()


class Like(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
