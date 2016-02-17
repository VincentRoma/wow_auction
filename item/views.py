from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .models import Item, Watch
from hotel.models import Sell
from django.db.models import Avg, Sum
from api import views as API
from hotel.serializers import SellSerializer
from .serializers import ItemSerializer


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



# ViewSets define the view behavior.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        item, created = Item.objects.get_or_create(item_id=pk)
        if created or not item.name:
            item_temp = API.get_item(pk)
            item.name=item_temp['name']
            item.save()
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def auctions(self, request, pk=None):
        auctions = Sell.objects.filter(item=pk)
        serializer = SellSerializer(auctions[:100], many=True)

        if auctions:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)
