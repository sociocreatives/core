from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Faq(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return (self.title)

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return (self.title)

class AboutHeader(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return (self.title)

class Partners(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return (self.title)

class Terms(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return (self.title)
