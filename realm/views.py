from django.shortcuts import render
from .models import Realm
from hotel.models import Sell, Sold
from item.models import Item

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

    # Remove sold item from current house
    old_house = Sell.objects.all()
    remove_sold(old_house, response['auctions'])

    for realm in response['realms']:
        current_realm = Realm.objects.get_or_create(name=realm['name'])

    for auction in response['auctions']:
        item = Item.objects.get_or_create(item_id=auction['item'])
        sell = Sell.objects.get_or_create(auction_id=auction['auc'])

        if sell[1]:
            sell[0].auction_id=auction['auc']
            sell[0].realm=current_realm[0]
            sell[0].item=item[0]
            sell[0].owner=auction['owner']
            sell[0].bid=auction['bid']
            sell[0].buyout=auction['buyout']
            sell[0].quantity=auction['quantity']
            sell[0].timeLeft=auction['timeLeft']
            sell.save()


def remove_sold(old, new):
    import timeit
    start_time = timeit.default_timer()

    # Flatten new list!
    flattened = []
    for row in new:
        flattened.append(row['auc'])

    # Match old with new if unsell
    for auction in old:
        if auction.auction_id not in flattened:
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
