from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


# Create your models here.
class Pet(models.Model):
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'
    TYPE_CHOICES = [(TYPE_CHOICE_DOG, 'Dog'), (TYPE_CHOICE_CAT, 'Cat'), (TYPE_CHOICE_PARROT, 'Parrot')]

    type = models.CharField(max_length=6, choices=TYPE_CHOICES)
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(
        upload_to='pets'
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
