from django.urls import path
from shop.api.views import (
    registerShopOwner, loginShopOwner, logoutShopOwner,updateShopOwnerProfile,delete_shop_owner,
    listShops, createShop, viewshopDetail,shopDetail,
    createProduct, productHandler,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path

urlpatterns = [
    # tocken
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Authentication endpoints
    path('auth/register/', registerShopOwner, name='register-shop-owner'),
    path('auth/login/', loginShopOwner, name='login-shop-owner'),
    path('auth/logout/', logoutShopOwner, name='logout-shop-owner'),
    path('auth/update-profile/', updateShopOwnerProfile, name='update-shop-owner-profile'),
    path('auth/delete-profile/', delete_shop_owner, name='delete-shop-owner'),

    # Shop endpoints
    path('shops/', listShops, name='list-shops'),
    path('shops/create/', createShop, name='create-shop'),
    path('shops/<int:shop_id>/', shopDetail, name='view-shop-detail'),
    path('shops/view/<int:shop_id>/', viewshopDetail, name='view-shop-detail'),

    # Product endpoints
    # path('products/', listProducts, name='list-products'),
    path('products/<int:product_id>/', productHandler, name='product-handler'),
    path('products/create/', createProduct, name='create-product'),
]
