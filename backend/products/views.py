from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404

from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        email  = serializer.validated_data.pop('email')
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

        # send a django signal


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_field = 'id


product_detail_view = ProductDetailAPIView.as_view()


class ProductListAPIView(StaffEditorPermissionMixin, generics.ListAPIView,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_view = ProductListAPIView.as_view()


class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            # instance.save()


product_update_view = ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, ]
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_delete_view = ProductDeleteAPIView.as_view()


# class ProddctMixinView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs);
#         return self.list(request, *args, **kwargs);

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs);

#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = title
#         serializer.save(content=content)

#     def perform_update(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def perform_destroy(self, instance):
#         return self.destroy(request, *args, **kwargs)


# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == 'GET':

#         # urls
#         # get single product
#         if pk is not None:
#             obj = get_object_or_404(Product, pk=pk)
#             serializer = ProductSerializer(obj, many = False).data
#             return Response(serializer)
#         # get all products list view
#         queryset = Product.objects.all()
#         serializer = ProductSerializer(queryset, many=True).data
#         return Response(serializer)

#     if method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response(serializer.errors)
