import random
from django.db import models

from consulting.utils import get_filename_ext
# Create your models here.


def get_team_image_name(instance, filename):
    digits = random.randint(800, 111111)
    name, ext = get_filename_ext(filename)
    final_name = '{name}{ext}'.format(name=digits, ext=ext)
    return 'team/{final_name}'.format(final_name=final_name)


def get_about_image_name(instance, filename):
    digits = random.randint(800, 111111)
    name, ext = get_filename_ext(filename)
    final_name = '{name}{ext}'.format(name=digits, ext=ext)
    return 'aboutus/{final_name}'.format(final_name=final_name)


def get_company_image_name(instance, filename):
    digits = random.randint(1, 500)
    img_name = 'company-' + str(digits)
    name, ext = get_filename_ext(filename)
    final_name = '{name}{ext}'.format(name=img_name, ext=ext)
    return 'company/{final_name}'.format(final_name=final_name)


def get_whoweare_image_name(instance, filename):
    digits = random.randint(1, 500)
    name, ext = get_filename_ext(filename)
    final_name = '{name}{ext}'.format(name=name, ext=ext)
    return 'whoweare/{final_name}'.format(final_name=final_name)


def get_logo_image_name(instance, filename):
    digits = random.randint(1, 500)
    img_name = 'logo-' + str(digits)
    name, ext = get_filename_ext(filename)
    final_name = '{name}{ext}'.format(name=img_name, ext=ext)
    return 'logo/{final_name}'.format(final_name=final_name)


class Team(models.Model):
    image = models.ImageField(upload_to=get_team_image_name)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MessageFromTeam(models.Model):
    author = models.ForeignKey(Team, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.author.name


class AboutUs(models.Model):
    image = models.ImageField(upload_to=get_about_image_name)
    title = models.CharField(max_length=400)
    details = models.TextField()

    def __str__(self):
        return self.title


class AboutCompany(models.Model):
    image = models.ImageField(upload_to=get_company_image_name)
    title = models.CharField(max_length=50)
    details = models.TextField()

    def __str__(self):
        return self.title


class CompanyStrategy(models.Model):
    name = models.CharField(max_length=30)
    length = models.IntegerField()

    def __str__(self):
        return self.name


class WhoWeAre(models.Model):
    strategy = models.ManyToManyField(CompanyStrategy, blank=True)
    image = models.ImageField(upload_to=get_whoweare_image_name)
    title = models.CharField(max_length=80)
    sub_title = models.CharField(max_length=150)
    details = models.TextField()

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=150)
    details = models.TextField()
    strategy = models.ManyToManyField(CompanyStrategy, blank=True)

    def __str__(self):
        return 'Experience'


class GeneralInformation(models.Model):
    logo = models.ImageField(upload_to=get_logo_image_name, blank=True)
    logo_2 = models.ImageField(upload_to=get_logo_image_name, blank=True)
    details = models.TextField(blank=True)

    number = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    pinnest = models.URLField(blank=True)
    google = models.URLField(blank=True)
    skype = models.URLField(blank=True)

    def __str__(self):
        return 'General Information'
