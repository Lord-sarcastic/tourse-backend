from rest_framework import generics, permissions
from destination.models import (
    Attraction,
    Culture,
    Zone,
    UserAttractionFavourite,
    Comment,
)

from destination.serializers import (
    CultureSerializer,
    ZoneSerializer,
    AttractionSerializer,
    UserAttractionFavouriteSerializer,
    CommentSerializer,
)


class CultureList(generics.ListAPIView):
    serializer_class = CultureSerializer
    queryset = Culture.objects.all()


class CultureDetail(generics.RetrieveAPIView):
    serializer_class = CultureSerializer
    queryset = Culture.objects.all()
    lookup_field = 'slug'


class ZoneList(generics.ListAPIView):
    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()


class ZoneDetail(generics.RetrieveAPIView):
    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()
    lookup_field = 'slug'


class AttractionList(generics.ListAPIView):
    serializer_class = AttractionSerializer
    queryset = Attraction.objects.all()


class AttractionDetail(generics.RetrieveAPIView):
    serializer_class = AttractionSerializer
    queryset = Attraction.objects.all()
    lookup_field = 'slug'


class UserAttractionFavouriteList(generics.ListCreateAPIView):
    serializer_class = UserAttractionFavouriteSerializer
    queryset = UserAttractionFavourite.objects.all()


class UserAttractionFavouriteDelete(generics.DestroyAPIView):
    queryset = UserAttractionFavourite.objects.all()


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
