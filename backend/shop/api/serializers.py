from rest_framework import serializers
from ..models import Category, Shop, Product, ShopOwnerProfile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

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
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Product
        fields = ['id','name', 'visibility', 'original_price', 'sale_price', 'product_code', 'out_of_stock', 'category', 'shop']
    