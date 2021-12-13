from apps.posts.models import Post
from django.dispatch import receiver
from apps.posts.utils import post_slug
from django.db.models.signals import pre_save, post_save

@receiver(pre_save, sender=Post)
def create_slug(sender, instance, **kwargs):
    if instance.slug is None:
        post_slug(instance, save=False)

@receiver(post_save, sender=Post)
def save_slug(sender, instance, created, **kwargs):
    if created:
        post_slug(instance, save=True)
