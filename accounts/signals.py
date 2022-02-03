from django.db.models.signals import (
    pre_save, post_save, pre_delete, post_delete
)
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .models import Account

@receiver(post_save, sender=Account)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
