from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from shop.models import Category
from shop.api.serializers import CategorySerializer
from django.db import IntegrityError


# List categories belonging to the shop owner's products
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listCategories(request):
    shop_owner = request.user.shopownerprofile
    categories = Category.objects.filter(shop_owner=shop_owner)  # Filter by shop owner
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


# Create a new category
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createCategory(request):
    shop_owner = request.user.shopownerprofile  # Get the authenticated user's shop owner profile
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save(shop_owner=shop_owner)  # Automatically assign the shop owner
            return Response(serializer.data, status=201)
        except IntegrityError:
            return Response({'error': 'You have already created a category with the same name.'})
    return Response(serializer.errors, status=400)




# update, or delete a specific category
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def categoryDetail(request, category_id):
    try:
        shop_owner = request.user.shopownerprofile
        category = Category.objects.get(id=category_id, shop_owner=shop_owner)  # Ensure ownership
    except Category.DoesNotExist:
        return Response({"error": "Category not found or not owned by you."}, status=404)

    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return Response({"message": "Category deleted successfully."}, status=204)

