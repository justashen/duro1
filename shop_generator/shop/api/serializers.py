from rest_framework import serializers
from ..models import Category, Shop, Product, SupplierProfile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Include all fields from the Category model

class SupplierProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierProfile
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    supplier = SupplierProfileSerializer()  # Nested Serializer

    class Meta:
        model = Shop
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested Serializer
    shops = ShopSerializer(many=True)  # Nested Serializer for related shops

    class Meta:
        model = Product
        fields = '__all__'
