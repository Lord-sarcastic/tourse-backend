from django.db import models

from backend.models import SlugifiedModel, TimeStampedModel


class Culture(SlugifiedModel, TimeStampedModel):
    name = models.charField(max_length=32)
    description = models.TextField()
