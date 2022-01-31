from django.db import models

from photologue.models import Gallery

from authentify.models import User
from backend.models import SlugifiedModel, TimeStampedModel
from destination.models import Zone


class Attraction(SlugifiedModel, TimeStampedModel):
    name = models.CharField(max_length=32)
    description = models.TextField()
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserAttractionFavourite(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "attraction")
    
    def __str__(self):
        return self.user.username


class Comment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username
