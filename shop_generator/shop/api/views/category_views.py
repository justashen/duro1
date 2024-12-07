from rest_framework.response import Response
from rest_framework.decorators import api_view
from shop.models import Category
from shop.api.serializers import CategorySerializer

@api_view(['GET'])
def listCategories(request):
    """Retrieve all categories."""
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createCategory(request):
    """Create a new category."""
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
