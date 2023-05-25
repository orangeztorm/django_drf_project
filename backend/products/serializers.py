from rest_framework import serializers

from rest_framework.reverse import reverse

from .models import Product

from . import validators

from api.serializer import UserPublicSerializer


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source= 'user', read_only=True)
    my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(
        validators=[validators.unique_product_title, validators.validate_title_no_hello,])

    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            # 'email',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'my_user_data'
        ]
        
    def get_my_user_data(self, obj):
        return {
            'username': obj.user.username,
            
        }
        
    
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(
    #             f'{value} is already a product name.')
    #     return value

    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title')
    #     return instance

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-edit', kwargs={'pk': obj.pk}, request=request)
        # return '/api/products/{pk}/'.format(pk=obj.pk)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj.id, Product):
            return None
        return obj.get_discount()
