from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Zone(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to="zone_covers")
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("zone_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
