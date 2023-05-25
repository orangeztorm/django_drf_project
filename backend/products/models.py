from decimal import Decimal
from django.db import models
from django.conf import settings
from django.db.models.query import QuerySet
from django.db.models import Q

# Create your models here.

user = settings.AUTH_USER_MODEL  # 'auth.User'


class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query,user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = qs.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs


class ProductManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset.is_public().search(query, user)


class Product(models.Model):
    # pk
    user = models.ForeignKey(
        user, null=True, on_delete=models.SET_NULL, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        decimal_places=2, max_digits=15, default=Decimal('99.99'))
    public = models.BooleanField(default=True)
    
    objects  = ProductManager()

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return '122.00'
