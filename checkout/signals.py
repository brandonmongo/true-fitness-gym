from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def _update_on_save(sender, instance, created, **kwargs):
    """
    update total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def _update_on_delete(sender, instance, **kwargs):
    """
    update total on lineitem delete
    """
    instance.order.update_total()
