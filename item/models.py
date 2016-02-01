from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
import math
from datetime import timedelta
from django.utils import timezone
from django.db.models import Avg, Sum


class Item(models.Model):
    name = models.CharField(max_length=200, null=True)
    item_id = models.PositiveIntegerField(default=None)
    buy_price = models.PositiveIntegerField(null=True)
    item_class = models.PositiveIntegerField(null=True)
    sub_class = models.PositiveIntegerField(null=True)
    level = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField('now')

    class Meta:
        ordering = ['item_id']

    def __str__(self):
        return 'Item {}'.format(self.item_id)


class Watch(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='watchs')

    price = models.PositiveIntegerField(default=0)
    inferior_to = models.BooleanField(default=True)

    def watch(self):
        from hotel.models import Sell
        if not self.item.name:
            pass
            #self.item.get_name();
        sells = Sell.objects.filter(item=self.item).values('owner').order_by('owner').annotate(total=Sum('quantity'), price=Sum('buyout'))
        for sell in sells:
            unit_price = math.trunc(sell['price']/sell['total'])
            time_limit = timezone.now() - timedelta(days=3)
            offer = Offer.objects.filter(item=self.item, seller=sell['owner'], unit_price=unit_price, created_at__gt=time_limit)
            if not offer:
                Offer.objects.create(
                    item = self.item,
                    seller = sell['owner'],
                    unit_price = unit_price,
                    created_at = timezone.now()
                )


class Offer(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='offers')

    seller = models.CharField(max_length=200, null=True)
    unit_price = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(null=True)


@receiver(pre_save,sender=Item)
def my_callback(sender, instance, *args, **kwargs):
    instance.created_at = timezone.now()

@receiver(pre_save,sender=Offer)
def my_callback(sender, instance, *args, **kwargs):
    instance.created_at = timezone.now()

@receiver(pre_save,sender=Watch)
def my_callback(sender, instance, *args, **kwargs):
    instance.watch()
