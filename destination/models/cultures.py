from django.db import models

from photologue.models import Gallery
from backend.models import SlugifiedModel, TimeStampedModel


class Culture(SlugifiedModel, TimeStampedModel):
    name = models.CharField(max_length=32)
    description = models.TextField()
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    zone = models.ForeignKey('Zone', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name