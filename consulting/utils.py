import os
import random
import string
from django.utils.text import slugify


def get_unique_string(size=10, char=string.ascii_lowercase):
    return ''.join(char for _ in range(size))


def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def get_unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{string}".format(slug=slug, string=get_unique_string(size=20))
        return get_unique_slug_generator(instance, new_slug=new_slug)
    return slug


def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext