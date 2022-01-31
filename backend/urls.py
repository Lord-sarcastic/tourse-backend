from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include([
        path("", include("dj_rest_auth.urls")),
        path("registration/", include("dj_rest_auth.registration.urls")),
    ])),
    path('destination/', include('destination.urls')),
]
