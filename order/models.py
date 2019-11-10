from django.db import models

# Create your models here.


class Order(models.Model):
    """order model to store order object"""

    user_profile = models.ForeignKey(
        'user.UserProfile', on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.DecimalField(max_digits=6, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.order_date
