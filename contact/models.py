from django.db import models

from service.models import Service
# Create your models here.


class FormContact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField()
    timestrimp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Quote(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    number = models.IntegerField()
    timestrimp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
