from django.db import models

# Create your models here.

AVAILABILITY = (
    (True, "Available"),
    (False, "Unavailable")
)


class PT(models.Model):
    full_name = models.CharField(max_length=70, blank=False, unique=True)
    slug = models.SlugField(max_length=70, blank=False, unique=True)
    opening_statement = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    availability = models.BooleanField(choices=AVAILABILITY, default=True, blank=False)
    contact_number = models.CharField(max_length=12, blank=False)
    PT_image = models.ImageField(blank=True)

    def __str__(self):
        return self.full_name

