from rest_framework import serializers

from photologue.models import Photo, Gallery

from destination.models import (
    Attraction,
    Culture,
    Zone,
    UserAttractionFavourite,
    Comment,
)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Gallery
        fields = "__all__"


class AttractionSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer()

    class Meta:
        model = Attraction
        fields = "__all__"


class CultureSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer()

    class Meta:
        model = Culture
        fields = "__all__"


class ZoneSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer()
    cover = PhotoSerializer()

    class Meta:
        model = Zone
        fields = "__all__"


class UserAttractionFavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAttractionFavourite
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
