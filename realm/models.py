from django.db import models

class Realm(models.Model):
    name = models.CharField(max_length=100)

    def fetch_auction(self):
        from api.views import get_auction
        resource = get_auction()
        return resource
