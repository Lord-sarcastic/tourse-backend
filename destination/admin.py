from django.contrib import admin

from destination.models import (
    Zone,
    Culture,
    Attraction,
    UserAttractionFavourite,
    Comment,
)

admin.site.register(Zone)
admin.site.register(Culture)
admin.site.register(Attraction)
admin.site.register(UserAttractionFavourite)
admin.site.register(Comment)
