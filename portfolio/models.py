import random
from django.db import models
from django.urls import reverse

from category.models import Category
from consulting.utils import get_filename_ext
from service.models import Service
# Create your models here.


def get_portfolio_image_name(instance, filename):
    digits = random.randint(500, 8888)
    name, ext = get_filename_ext(filename)
    final_name = '{name}{ext}'.format(name=digits, ext=ext)
    return 'portfolio/{final_name}'.format(final_name=final_name)


def get_default_category():
    try:
        return Category.objects.get(name='other').pk
    except Category.DoesNotExist:
        return None


class Portfolio(models.Model):

    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    # category = models.ForeignKey(Category,
    #                              on_delete=models.SET_DEFAULT,
    #                              related_query_name='portfolio_category',
    #                              default=get_default_category
    #                              )
    title = models.CharField(max_length=150)
    details = models.TextField()
    image = models.ImageField(upload_to=get_portfolio_image_name)

    image_2 = models.ImageField(upload_to=get_portfolio_image_name, blank=True)
    image_3 = models.ImageField(upload_to=get_portfolio_image_name, blank=True)
    details_2 = models.TextField(blank=True)

    timestrimp = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('portfolio:portfolio_details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pk', )

