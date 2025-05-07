from django.db import models

class Product(models.Model):
    # The barcode field, which should be unique for each product
    barcode = models.CharField(max_length=100, unique=True)
    
    # The name of the product
    name = models.CharField(max_length=100)
    
    # The price of the product, with support for decimals
    price = models.DecimalField(max_digits=10, decimal_places=2)
