from django.db import models

# Create your models here.
class Holding(models.Model):
    company = models.CharField(max_length=100)
    trade_date = models.DateField()
    quantity = models.IntegerField(null=True, blank=True)
    unit_per_share = models.DecimalField(max_digits=10, decimal_places=2)
    brokerage = models.CharField(max_length=100, null=True, blank=True)