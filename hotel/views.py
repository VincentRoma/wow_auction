from django.shortcuts import render
from realm.models import Realm
from .models import Sell
from rest_framework import viewsets
from .serializers import SellSerializer

def realms(request):
    realms = Realm.objects.all()
    context = {'realms': realms}
    return render(request, 'hotel/index.html', context)

def realm(request, realm_id):
    from .models import Sell
    realm = Realm.objects.get(id=realm_id)
    if realm:
        sells = Sell.objects.filter(realm_id=realm.id)[:100]
        context = {'realm': realm, 'sells': sells}
        return render(request, 'hotel/realm.html', context)


# ViewSets define the view behavior.
class SellViewSet(viewsets.ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
