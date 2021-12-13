import os
from PIL import Image
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Heed(models.Model):
    title = models.CharField(max_length=55)
    message = models.TextField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'heed'
        verbose_name_plural = 'heeds'
        ordering = ['-created']

    def __str__(self):
        return self.title
