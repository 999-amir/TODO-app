from django.db import models
from .managers import CostumeUserManager
from django.contrib.auth.models import AbstractBaseUser


class CostumeUser(AbstractBaseUser):
    email = models.EmailField(max_length=250, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = CostumeUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
