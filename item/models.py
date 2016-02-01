from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=200, null=True)
    item_id = models.PositiveIntegerField(default=None)
    buy_price = models.PositiveIntegerField(null=True)
    item_class = models.PositiveIntegerField(null=True)
    sub_class = models.PositiveIntegerField(null=True)
    level = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField('now')


class Watch(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='watchs')

    price = models.PositiveIntegerField(default=0)
    inferior_to = models.BooleanField(default=True)


class Offer(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='offers')

    seller = models.CharField(max_length=200, null=True)
    unit_price = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField('now')


@receiver(pre_save,sender=Item)
def my_callback(sender, instance, *args, **kwargs):
    instance.created_at = timezone.now()

@receiver(pre_save,sender=Offer)
def my_callback(sender, instance, *args, **kwargs):
    instance.sold_at = timezone.now()
