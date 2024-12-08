from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from shop.models import ShopOwnerProfile
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from rest_framework import status

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# REGISTER
@api_view(['POST'])
def registerShopOwner(request):
    data = request.data
    required_fields = ['username', 'password', 'email']
    
    # Check for missing fields
    for field in required_fields:
        if field not in data:
            return Response({'error': f"'{field}' field is required."}, status=400)

    try:
        # Create the user
        user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            email=data['email'],
            first_name=data.get('first_name',''),
            last_name=data.get('last_name','')
        )
        # Create the ShopOwner profile
        ShopOwnerProfile.objects.create(user=user)
        
        # Generate tokens
        tokens = get_tokens_for_user(user)
        return Response({'user': user.username, 'tokens': tokens}, status=201)
    
    except IntegrityError:
        # Handle duplicate username or email
        return Response({'error': 'Username or email already exists.'}, status=400)
    
    except Exception as e:
        # Catch other exceptions
        return Response({'error': f"An error occurred: {str(e)}"}, status=500)
    
# LOGIN
@api_view(['POST'])
def loginShopOwner(request):
    data = request.data
    required_fields = ['username', 'password']
    
    # Check for missing fields
    for field in required_fields:
        if field not in data:
            return Response({'error': f"'{field}' field is required."}, status=400)
    
    user = authenticate(username=data['username'], password=data['password'])
    if user:
        try:
            # Generate tokens
            tokens = get_tokens_for_user(user)
            return Response({'user': user.username, 'tokens': tokens}, status=200)
        except Exception as e:
            return Response({'error': f"An error occurred: {str(e)}"}, status=500)
    
    return Response({'error': 'Invalid credentials.'}, status=401)
# LOGOUT
@api_view(['POST'])
def logoutShopOwner(request):
    try:
        # Placeholder message for client-side token removal
        return Response({"message": "Logout successful. Tokens should be cleared client-side."}, status=200)
    except Exception as e:
        return Response({'error': f"An error occurred: {str(e)}"}, status=500)

# UPDATE PROFILE
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def updateShopOwnerProfile(request):
    """Update the shop owner's username, email, and password."""
    user = request.user  # Get the logged-in user
    data = request.data

    # Update username if provided
    if 'username' in data:
        user.username = data['username']
    
    # Update email if provided
    if 'email' in data:
        user.email = data['email']
        
    if 'first_name' in data:
        user.first_name = data['first_name']
        
    if 'last_name' in data:
        user.last_name = data['last_name']
        

    # Update password if provided
    if 'password' in data:
        new_password = data['password']
        
        # Optionally: Add validation for password strength (e.g., min length)
        if len(new_password) < 6:
            return Response({"error": "Password too short, must be at least 6 characters."}, status=400)

        user.set_password(new_password)  # Hash the password before saving

    user.save()  # Save the updated user object
    return Response({"message": "Shop Owner profile updated successfully."}, status=200)

# DELETE
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])  # Ensure only authenticated users can delete
def delete_shop_owner(request):
    user = request.user #user = current authenticated user
    if user != request.user:
        return Response({"message": "You can only delete your own profile."}, status=status.HTTP_403_FORBIDDEN)
    try:
        # The user that sent the request (i.e., the current authenticated ShopOwner)
        user = request.user
        user.delete()  # Delete the user (ShopOwner)
        return Response({"message": "Shop Owner deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)