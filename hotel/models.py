from django.db import models
from item.models import Item
from realm.models import Realm
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone


class Sell(models.Model):
    realm = models.ForeignKey(Realm, on_delete=models.CASCADE, related_name='sells', null=True)

    item = models.PositiveIntegerField(null=True)
    auction_id = models.CharField(max_length=50, null=True)
    owner = models.CharField(max_length=50, null=True)
    bid = models.PositiveIntegerField(null=True)
    buyout = models.PositiveIntegerField(null=True)
    quantity = models.IntegerField(default=1, null=True)
    timeLeft = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField('now', null=True)
    batch = models.IntegerField(null=True)

class Sold(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='solds')
    realm = models.ForeignKey(Realm, on_delete=models.CASCADE, related_name='solds')

    auction_id = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    bid = models.PositiveIntegerField()
    buyout = models.PositiveIntegerField()
    quantity = models.IntegerField(default=1)
    sold_at = models.DateTimeField('now')
    created_at = models.DateTimeField('now')


@receiver(pre_save,sender=Sell)
def my_callback(sender, instance, *args, **kwargs):
    instance.created_at = timezone.now()

@receiver(pre_save,sender=Sold)
def my_callback(sender, instance, *args, **kwargs):
    instance.sold_at = timezone.now()
