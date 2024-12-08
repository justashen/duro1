from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from shop.models import Shop
from shop.api.serializers import ShopSerializer
from django.db import IntegrityError


# List all shops owned by the authenticated user
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Anyone can access the list of shops
def listShops(request):
    # Fetch shops that are publicly visible (if needed, filter based on permissions)
    if request.user.is_staff or request.user.is_superuser:
        shops = Shop.objects.all()
    else:
        shops = Shop.objects.filter(shop_owner=request.user.shopownerprofile)
    serializer = ShopSerializer(shops, many=True)
    return Response(serializer.data)


# Create a new shop - Automatically assign the authenticated user as the shop owner
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Only authenticated users can create a shop
def createShop(request):
    serializer = ShopSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save(shop_owner=request.user.shopownerprofile)  # Assign shop owner
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update, or delete a specific shop
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])  # Only authenticated users can update or delete shops
def shopDetail(request, shop_id):
    try:
        # Ensure the shop belongs to the authenticated user
        shop = Shop.objects.get(id=shop_id, shop_owner=request.user.shopownerprofile)
    except Shop.DoesNotExist:
        return Response({"error": "Shop not found or you do not have permission to access it."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        # Update shop details
        serializer = ShopSerializer(shop, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                serializer.save(shop_owner=request.user.shopownerprofile)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except IntegrityError:
                return Response({"error": "The domain_name must be unique."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete shop
        shop.delete()
        return Response({"message": "Shop deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# Retrieve a specific shop
@permission_classes([AllowAny])
@api_view(['GET'])
def viewshopDetail(request, shop_id):
    try:
        # Ensure the shop belongs to the authenticated user
        shop = Shop.objects.get(id=shop_id)
    except Shop.DoesNotExist:
        return Response({"error": "Shop not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ShopSerializer(shop)
    return Response(serializer.data)