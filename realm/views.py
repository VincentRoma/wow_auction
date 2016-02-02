from django.shortcuts import render
from .models import Realm
from hotel.models import Sell, Sold
from item.models import Item
from django.utils import timezone

def scan(request, realm_id):
    auction = None
    realm = Realm.objects.get(id=realm_id)
    if realm:
        auction = realm.fetch_auction()
        if auction:
            persist_auctions(auction)
    context = {'auction': auction}
    return render(request, 'realm/index.html', context)


def persist_auctions(auctions):
    from api.views import handle_request
    # Ask for the json from the URL
    response = handle_request(auctions)
    bulk_object_auction = []
    bulk_object_item = []
    # Remove sold item from current house
    # old_house = Sell.objects.all()
    # remove_sold(old_house, response['auctions'])
    iteration = Sell.objects.last()
    if iteration:
        iteration = iteration.batch + 1
    else:
        iteration = 1

    for realm in response['realms']:
        current_realm = Realm.objects.get_or_create(name=realm['name'])

    for auction in response['auctions']:
        bulk_object_item.append(Item(item_id=auction['auc']))
        bulk_object_auction.append(Sell(
            auction_id=auction['auc'],
            realm=current_realm[0],
            item=auction['item'],
            owner=auction['owner'],
            bid=auction['bid'],
            buyout=auction['buyout'],
            quantity=auction['quantity'],
            timeLeft=auction['timeLeft'],
            created_at=timezone.now(),
            batch=iteration
        ))
    Item.objects.bulk_create(bulk_object_item)
    Sell.objects.bulk_create(bulk_object_auction)


def remove_sold(old, new):
    import timeit
    start_time = timeit.default_timer()

    # Flatten new list!
    flattened = []
    for row in new:
        flattened.append(row['auc'])

    # Match old with new if unsell
    for auction in old:
        if int(auction.auction_id) not in flattened:
            Sold.objects.create(
                item=auction.item,
                realm=auction.realm,
                auction_id=auction.auction_id,
                owner=auction.owner,
                bid=auction.bid,
                buyout=auction.buyout,
                quantity=auction.quantity,
                created_at=auction.created_at
            )
            auction.delete()
    elapsed = timeit.default_timer() - start_time
    print elapsed
