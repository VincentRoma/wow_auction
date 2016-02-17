from django.conf.urls import patterns, include, url
from django.contrib import admin
from hotel import views as HotelViews
from realm import views as RealmViews
from item import views as ItemViews
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'sell', HotelViews.SellViewSet)
router.register(r'item', ItemViews.ItemViewSet)

urlpatterns = patterns('',

    url(r'^', include(router.urls)),
    url(r'^item/(?P<item_id>[0-9]+)/$', ItemViews.item, name='item'),
    url(r'^(?P<realm_id>[0-9]+)/scan/$', RealmViews.scan, name='scan'),
    url(r'^(?P<realm_id>[0-9]+)/auctions/$', HotelViews.realm, name='auctions'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
