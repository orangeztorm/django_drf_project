import json
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer

@api_view(['POST']) 
def api_home(request, *args, **kwargs):
    # instance = Product.objects.all().order_by('?').first()
    # data = {}
    # if instance:
    #     data = ProductSerializer(instance).data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid( raise_exception=True):
        serializer = serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
