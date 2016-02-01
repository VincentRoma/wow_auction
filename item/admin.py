from django.contrib import admin
from .models import Watch


class WatchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Watch, WatchAdmin)
