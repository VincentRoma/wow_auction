from django.shortcuts import render
from realm.models import Realm

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
