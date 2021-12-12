import uuid
import random
from django.dispatch import receiver
from apps.users.models import User, Account
from django.db.models.signals import pre_save, post_save
from django.dispatch.dispatcher import receiver

@receiver(pre_save, sender=User)
def create_account(sender, instance, **kwargs):
    if instance.username is None:
        instance.username = uuid.uuid1()

    
@receiver(post_save, sender=User)
def save_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
        def hex(): return random.randint(0, 255)
        instance.account.hexcode = '#%02X%02X%02X' % (hex(), hex(), hex())
        instance.account.save()
        instance.save()

        

    

    
