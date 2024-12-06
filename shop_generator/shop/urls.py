from django.urls import path, include

urlpatterns = [
    path('', include('shop.api.urls')),  # Include API URLs
]