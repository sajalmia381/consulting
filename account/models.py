import random
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from consulting.utils import get_filename_ext
# Create your models here.


def new_user_image_name(instance, filename):
    digits = random.randint(1, 888888)
    name, ext = get_filename_ext(filename)
    final_name = '{name}{ext}'.format(name=digits, ext=ext)
    return 'account/{final_name}'.format(final_name=final_name)


class NewUserManager(models.Manager):

    def create_user(self, email, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('User Must Have a Valid Email Address')
        if not password:
            raise ValueError('user Must Have a Valid Password')

        user_obj = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )
        user_obj.set_password = password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)

    def create_staff_user(self, email,  full_name=None, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True
        )
        return user

    def create_admin_user(self, email, full_name=None, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class NewUser(AbstractBaseUser):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=150, unique=True)
    # image = models.ImageField(upload_to=new_user_image_name, blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = NewUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_lavel):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
