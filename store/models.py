from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=300, null=False)
    description = models.CharField(max_length=300, null=False)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    buying_price = models.DecimalField(max_digits=8, decimal_places=2)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.name
