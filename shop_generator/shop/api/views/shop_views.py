from rest_framework.response import Response
from rest_framework.decorators import api_view
from shop.models import Shop
from shop.api.serializers import ShopSerializer

@api_view(['GET'])
def listShops(request):
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createShop(request):
    serializer = ShopSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
