from django.urls import path, include

from . import views

app_name = 'destination'

urlpatterns = [
    path('cultures/', include([
        path('', views.CultureList.as_view(), name='culture_list'),
        path('<slug:slug>/', views.CultureDetail.as_view(), name='culture_detail'),
    ])),
    path('zones/', include([
        path('', views.ZoneList.as_view(), name='zone_list'),
        path('<slug:slug>/', views.ZoneDetail.as_view(), name='zone_detail'),
    ])),
    path('attractions/', include([
        path('', views.AttractionList.as_view(), name='attraction_list'),
        path('<slug:slug>/', views.AttractionDetail.as_view(), name='attraction_detail'),
    ])),
    path('user_attraction_favourites/', include([
        path('', views.UserAttractionFavouriteList.as_view(), name='user_attraction_favourite_list'),
        path('<int:pk>/', views.UserAttractionFavouriteDelete.as_view(), name='user_attraction_favourite_delete'),
    ])),
    path('comment/', views.CommentList.as_view(), name='comment_list'),
]