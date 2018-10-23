from django.db import models

class Product(models.Model):
    _id = models.IntegerField(default=4,primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    qty = models.IntegerField(default=4)