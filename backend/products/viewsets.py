from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     if not instance.content:
    #         instance.content = instance.title
    #         instance.save()
    
    
class ProductGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

