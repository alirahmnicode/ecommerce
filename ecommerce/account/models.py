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


class Profile(models.Model):
    user = models.OneToOneField("CustomUser", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    address = models.TextField(blank=False, help_text=_("street 11, block 4"))
    postal_code = models.TextField(max_length=20, help_text=_("312342131232"))
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.user.phone
