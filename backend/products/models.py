from decimal import Decimal
from django.db import models
from django.conf import settings

# Create your models here.

user = settings.AUTH_USER_MODEL  # 'auth.User'


class Product(models.Model):
    # pk
    user = models.ForeignKey(
        user, null=True, on_delete=models.SET_NULL, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        decimal_places=2, max_digits=15, default=Decimal('99.99'))

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return '122.00'
