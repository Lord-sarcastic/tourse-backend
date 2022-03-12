from rest_framework import generics, permissions
from destination.permissions import IsUserAsOwner
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
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserAttractionFavouriteSerializer

    def get_queryset(self):
        return UserAttractionFavourite.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserAttractionFavouriteDelete(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsUserAsOwner]
    queryset = UserAttractionFavourite.objects.all()


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
