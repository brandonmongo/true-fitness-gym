from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Product(models.Model):
    Category = models.CharField(max_length=255, blank=True)
    Name = models.CharField(max_length=255, blank=True)
    Brand = models.CharField(max_length=255, blank=True)
    Size = models.CharField(max_length=100, blank=True)
    has_weight = models.BooleanField(default=False, blank=True, null=True)
    Flavor = ArrayField(
        models.CharField(max_length=30, blank=True), blank=True)
    Servings = models.PositiveIntegerField(blank=True)
    Rating = models.DecimalField(
        max_digits=3, decimal_places=1, blank=True, null=True)
    FlavorRating = models.CharField(max_length=3, blank=True)
    Reviews = models.PositiveIntegerField(blank=True)
    Price = models.DecimalField(max_digits=8, decimal_places=2)
    product_description = models.TextField()
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.Name
