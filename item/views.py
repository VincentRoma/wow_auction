from django.shortcuts import render
from .models import Item, Watch
from hotel.models import Sell
from django.db.models import Avg, Sum



def item(request, item_id):
    item = Item.objects.get(id=item_id)
    stats = []
    stats.append({
                    'name': 'Currently selling',
                    'value': Sell.objects.filter(item__id=item_id).aggregate(Sum('quantity'))['quantity__sum']
                })
    stats.append({
                    'name': 'Average bid',
                    'value': Sell.objects.filter(item__id=item_id).aggregate(Avg('bid'))['bid__avg']
                })
    stats.append({
                    'name': 'Average buyout',
                    'value': Sell.objects.filter(item__id=item_id).aggregate(Avg('buyout'))['buyout__avg']
                })
    context = {'item': item, 'stats': stats}
    return render(request, 'item/index.html', context)


def watch():
    watchs = Watch.objects.all()
    for watch in watchs:
        watch.watch();
