import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager


class Users(AbstractBaseUser):
    #  max_length is ignored by integer field use validators
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, verbose_name="نام")
    last_name = models.CharField(max_length=30)
    # if it was int field, 0 at first will be deleted
    national_code = models.CharField(max_length=10, unique=True, db_index=True)
    birth_date = models.DateField()
    home_address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=10, unique=True, db_index=True)
    register_date = models.DateField()
    phone_number = models.CharField(max_length=11, unique=True)
    education = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "national_code"
    REQUIRED_FIELDS = ["first_name", "last_name", "birth_date", "home_address",
                       "postal_code", "register_date", "phone_number", "education"]


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
