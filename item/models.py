from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200, null=True)
    item_id = models.PositiveIntegerField(default=None)
    buy_price = models.PositiveIntegerField(null=True)
    item_class = models.PositiveIntegerField(null=True)
    sub_class = models.PositiveIntegerField(null=True)
    level = models.PositiveIntegerField(null=True)
