from rest_framework.response import Response
from rest_framework.decorators import api_view
from shop.models import Product
from shop.api.serializers import ProductSerializer

@api_view(['GET'])
def listProducts(request):
    products = Product.objects.filter(visibility=True)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
