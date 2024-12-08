from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from shop.models import Product, Shop
from shop.api.serializers import ProductSerializer


# Handle POST (create product)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProduct(request):
    """
    Create a new product (only for authenticated shop owners).
    """
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            try:
                # Ensure the shop belongs to the authenticated user
                shop = Shop.objects.get(id=request.data['shop'], shop_owner=request.user.shopownerprofile)
                

                # Save the product with the shop association
                serializer.save(shop=shop)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Shop.DoesNotExist:
                return Response({"error": "Invalid shop or permission denied."}, status=status.HTTP_403_FORBIDDEN)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Function to handle individual product actions (GET by ID, PUT, DELETE)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def productHandler(request, product_id=None):
    """
    Handles individual product actions:
    - GET by ID: Retrieve a specific product.
    - PUT: Update an existing product (shop owners only).
    - DELETE: Delete a product (shop owners only).
    """
    # Handle GET by ID
    if request.method == 'GET':
        if not product_id:
            return Response({"error": "Product ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id, visibility=True)  # Publicly visible product
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

    # Handle PUT (update product)
    if request.method == 'PUT':
        if not product_id:
            return Response({"error": "Product ID is required for updates."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id, shop__shop_owner=request.user.shopownerprofile)

            # Update the product
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({"error": "Product not found or permission denied."}, status=status.HTTP_404_NOT_FOUND)

    # Handle DELETE
    if request.method == 'DELETE':
        if not product_id:
            return Response({"error": "Product ID is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id, shop__shop_owner=request.user.shopownerprofile)
            product.delete()
            return Response({"message": "Product deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"error": "Product not found or permission denied."}, status=status.HTTP_404_NOT_FOUND)

    return Response({"error": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
