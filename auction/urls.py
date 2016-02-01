from django.conf.urls import patterns, include, url
from django.contrib import admin
from hotel import views as HotelViews
from realm import views as RealmViews
from item import views as ItemViews

urlpatterns = patterns('',

    url(r'^$', HotelViews.realms, name='home'),
    url(r'^item/(?P<item_id>[0-9]+)/$', ItemViews.item, name='item'),
    url(r'^(?P<realm_id>[0-9]+)/scan/$', RealmViews.scan, name='scan'),
    url(r'^(?P<realm_id>[0-9]+)/auctions/$', HotelViews.realm, name='auctions'),
    url(r'^admin/', include(admin.site.urls)),
)
