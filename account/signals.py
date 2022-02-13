from django.db.models.signals import (
    pre_save, post_save, pre_delete, post_delete
)
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .models import Account, Referral, Profile


@receiver(post_save, sender=Account)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        Profile.objects.create(user=instance)
        Referral.objects.create(user=instance)


@receiver(post_save, sender=Referral)
def create_ref_code(sender, instance, **kwargs):
    if instance.ref_code is not None and instance.is_used is True:
        Referral.objects.create(user=instance)
