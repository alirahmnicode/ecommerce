from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    phone = models.CharField(_("phone number"), unique=True, max_length=11)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone
