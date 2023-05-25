from rest_framework import serializers

class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookupp_field='pk',
        read_only=True,
    )
    tile = serializers.CharField(read_only=True)
 
class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    other_products = serializers.SerializerMethodField(read_only=True)
    
    def get_other_products(self, obj):
        return obj.product_set.all()
    