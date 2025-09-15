import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager


class Users(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    national_code = models.IntegerField(
        max_length=10, unique=True, db_index=True)
    bitrh_date = models.DateTimeField()
    home_address = models.CharField()
    postal_code = models.IntegerField(max_length=10)
    register_date = models.CharField()
    phone_number = models.IntegerField(max_length=11)
    eduacation = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FEILD = "national_code"
    REQUIRED_FIELDS = ["national_code", "phone_number"]
    objects = UserManager()

    def __str__(self):
        return (self.first_name + '\t' + self.last_name + ': ' + 
                self.national_code)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
