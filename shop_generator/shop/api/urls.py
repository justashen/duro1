from django.urls import path
from shop.api.views import (
    registerShopOwner, loginShopOwner, logoutShopOwner,updateShopOwnerProfile,delete_shop_owner,
    listShops, createShop,
    listProducts, createProduct,
    listCategories, createCategory,
)

urlpatterns = [
    # Authentication endpoints
    path('auth/register/', registerShopOwner, name='register-shop-owner'),
    path('auth/login/', loginShopOwner, name='login-shop-owner'),
    path('auth/logout/', logoutShopOwner, name='logout-shop-owner'),
    path('auth/update-profile/', updateShopOwnerProfile, name='update-shop-owner-profile'),
    path('auth/delete-profile/', delete_shop_owner, name='delete-shop-owner'),

    # Shop endpoints
    path('shops/', listShops, name='list-shops'),
    path('shops/create/', createShop, name='create-shop'),

    # Product endpoints
    path('products/', listProducts, name='list-products'),
    path('products/create/', createProduct, name='create-product'),

    # Category endpoints
    path('categories/', listCategories, name='list-categories'),
    path('categories/create/', createCategory, name='create-category'),
]
