from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from petstagram.accounts.managers import PetstagramUserManager


class PetstagramUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False
    )
    USERNAME_FIELD = 'email'

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    object = PetstagramUserManager()


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True
    )
    user = models.OneToOneField(
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True
    )

from .signals import *