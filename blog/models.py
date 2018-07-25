import random
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.conf import settings
from django.db.models import Q
from category.models import Category

from consulting.utils import get_filename_ext, get_unique_slug_generator
# Create your models here.


def get_image_name(instance, filename):
    random_name = random.randint(1, 9999999)
    name, ext = get_filename_ext(filename)
    full_name = '{name}{ext}'.format(name=random_name, ext=ext)
    return 'blog/{full_name}'.format(full_name=full_name)


def get_comment_image_name(instance, filename):
    random_name = random.randint(1, 9999999)
    name, ext = get_filename_ext(filename)
    full_name = '{name}{ext}'.format(name=random_name, ext=ext)
    return 'blog/comment/{full_name}'.format(full_name=full_name)


def tag_default():
    return Category.objects.get(name='other').pk


class Tag(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=tag_default)
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class BlogQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def search(self, query):
        look_up = (
            Q(title__icontains=query) |
            Q(paragraph__icontains=query)
        )
        return self.filter(look_up).distinct()


class BlogManager(models.Manager):
    def get_queryset(self):
        return BlogQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def search(self, query):
        return self.get_queryset().active().search(query)


class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to=get_image_name, blank=True)
    slug = models.SlugField(blank=True, null=True, max_length=500)
    title = models.CharField(max_length=500, unique=True)
    sub_title = models.CharField(max_length=400, blank=True)
    paragraph = models.TextField()
    sub_paragraph = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    timestrimp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = BlogManager()

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-timestrimp',)


def pre_save_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = get_unique_slug_generator(instance)


pre_save.connect(pre_save_slug, sender=Blog)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_comment_image_name, blank=True, default='blog/comment/default.png')
    full_name = models.CharField(max_length=25, blank=True)
    email = models.EmailField(blank=True)
    text = models.TextField()
    timestrimp = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_comment_image_name, blank=True, default='blog/comment/default.png')
    full_name = models.CharField(max_length=25, blank=True)
    email = models.EmailField(blank=True)
    text = models.TextField()
    timestrimp = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email