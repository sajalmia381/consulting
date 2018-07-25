import random
from django.db import models

# Create your models here.

from consulting.utils import get_filename_ext


def get_banner_image_name(instance, filename):
    digints = random.randint(1, 999999)
    name, ext = get_filename_ext(filename)
    final_name = '{name}{ext}'.format(name=digints, ext=ext)
    return 'banner/{final_name}'.format(final_name=final_name)


def get_partner_image_name(instance, filename):
    digints = random.randint(1, 999999)
    name, ext = get_filename_ext(filename)
    final_name = '{name}{ext}'.format(name=digints, ext=ext)
    return 'partner/{final_name}'.format(final_name=final_name)


def get_testimonial_image_name(instance, filename):
    digints = random.randint(1, 999999)
    name, ext = get_filename_ext(filename)
    final_name = '{name}{ext}'.format(name=digints, ext=ext)
    return 'testimonial/{final_name}'.format(final_name=final_name)


class IndexBanner(models.Model):
    title = models.CharField(max_length=45)
    details = models.TextField()
    image = models.ImageField(upload_to=get_banner_image_name)

    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to=get_partner_image_name)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('pk',)


class Achievement(models.Model):
    name = models.CharField(max_length=30)
    total = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to=get_testimonial_image_name)
    speach = models.TextField()

    def __str__(self):
        return self.name
