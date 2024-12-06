from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Category, Shop, Product, SupplierProfile
from .serializers import (
    CategorySerializer,
    ShopSerializer,
    ProductSerializer,
    SupplierProfileSerializer,
)

# Categories
@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Products
@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Shops
@api_view(['GET'])
def getShops(request):
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addShop(request):
    serializer = ShopSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Supplier Profiles
@api_view(['GET'])
def getSupplierProfiles(request):
    suppliers = SupplierProfile.objects.all()
    serializer = SupplierProfileSerializer(suppliers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addSupplierProfile(request):
    serializer = SupplierProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
