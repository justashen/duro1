from rest_framework import serializers
from ..models import Shop, Product, ShopOwnerProfile

class ShopOwnerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopOwnerProfile
        fields = '__all__'
    
class ShopSerializer(serializers.ModelSerializer):
    # shopOwner = ShopOwnerProfileSerializer()  # Nested Serializer

    class Meta:
        model = Shop
        exclude = ['shop_owner']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'visibility', 'original_price','image', 'sale_price', 'out_of_stock', 'shop']
    