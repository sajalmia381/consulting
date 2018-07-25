import random
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.urls import reverse

from category.models import Category
from consulting.utils import get_filename_ext, get_unique_string
# Create your models here.


def get_service_image_name(instance, filename):
    digits = random.randint(100, 500000)
    name, ext = get_filename_ext(filename)
    final_name = '{name}{ext}'.format(name=digits, ext=ext)
    return 'service/{final_name}'.format(final_name=final_name)


def get_unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{string}".format(slug=slug, string=get_unique_string(size=20))
        return get_unique_slug_generator(instance, new_slug=new_slug)
    return slug


def get_category_default():
    try:
        return Category.objects.get(name='other').pk
    except:
        return None


class Service(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=get_category_default)
    title = models.CharField(max_length=100)
    details = models.TextField()
    icon = models.ImageField(upload_to=get_service_image_name, blank=True)
    image = models.ImageField(upload_to=get_service_image_name)
    slug = models.CharField(max_length=50, blank=True)

    title_2 = models.CharField(max_length=100, blank=True)
    details_2 = models.TextField(blank=True)
    image_2 = models.ImageField(upload_to=get_service_image_name, blank=True)

    showcase_image_1 = models.ImageField(upload_to=get_service_image_name, blank=True)
    showcase_image_2 = models.ImageField(upload_to=get_service_image_name, blank=True)
    showcase_image_3 = models.ImageField(upload_to=get_service_image_name, blank=True)

    title_3 = models.CharField(max_length=100, blank=True)
    details_3 = models.TextField(blank=True)

    title_4 = models.CharField(max_length=100, blank=True)
    details_4 = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('service:service_details', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


def pre_save_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = get_unique_slug_generator(instance)


pre_save.connect(pre_save_slug, sender=Service)


def get_feature_image_name(instance, filename):
    digits = random.randint(1, 5000)
    new_name = 'feature' + str(digits)
    name, ext = get_filename_ext(filename)
    final_name = '{name}{ext}'.format(name=new_name, ext=ext)
    return 'feature/{final_name}'.format(final_name=final_name)


class Feature(models.Model):

    image = models.ImageField(upload_to=get_feature_image_name)
    title = models.CharField(max_length=250)
    details = models.TextField()

    def __str__(self):
        return self.title


class PriceTableFeature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PriceTable(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    details = models.ManyToManyField(PriceTableFeature, blank=True)

    def __str__(self):
        return self.title

