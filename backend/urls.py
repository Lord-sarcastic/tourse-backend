from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authentify.urls")),
    path("destination/", include("destination.urls")),
    path("photologue/", include("photologue.urls", namespace="photologue")),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
