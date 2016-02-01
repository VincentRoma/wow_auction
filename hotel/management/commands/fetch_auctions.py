from django.core.management.base import BaseCommand, CommandError
from realm.models import Realm
from realm.views import persist_auctions

class Command(BaseCommand):
    help = 'Refresh Auctions, detect sold item and activate watch function'

    def handle(self, *args, **options):
        realm = Realm.objects.get(id=1)
        print "Starting for {}".format(realm.name)
        if realm:
            auction = realm.fetch_auction()
            if auction:
                print "Start Persist Auction"
                persist_auctions(auction)

        # watchs = Watch.objects.all()
        # if watchs:
        #     for watch in watchs:
        #         watch.watch();

        self.stdout.write(self.style.SUCCESS('Successfully Fetched'))
