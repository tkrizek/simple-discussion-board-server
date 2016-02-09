from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Thread(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    # id, url, author?
    
    class Meta:
        ordering = ('created',)

class User(models.Model):
    username = models.CharField(max_length=30, blank=False)
