from django.db import models


class PricingModel(models.Model):
    price_per_time = models.DecimalField(max_length=4, decimal_places=2)
    price_per_distance = models.DecimalField(max_length=4, decimal_places=2)
    price_per_weight = models.IntegerField()      # weight in grams
    price_per_volume = models.IntegerField()      # volume in cubic mm
    service_tax = models.DecimalField(max_length=3, decimal_places=2)
