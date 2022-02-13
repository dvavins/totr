from django.dispatch import receiver
from django.db.models.signals import (
    pre_save, post_save, pre_delete, post_delete
)

from teams.models import Teams, Members, TodosGroup, TranxGroup


@receiver(post_save, sender=Teams)
def models_init(sender, instance, created, **kwargs):
    if created:
        TodosGroup.objects.create(team=instance)
        TranxGroup.objects.create(team=instance)





