from django.urls import path
from .views import (
    getCategories,
    addCategory,
    getProducts,
    addProduct,
    getShops,
    addShop,
    getSupplierProfiles,
    addSupplierProfile,
)

urlpatterns = [
    # Categories
    path('categories/', getCategories, name='get_categories'),
    path('categories/add/', addCategory, name='add_category'),

    # Products
    path('products/', getProducts, name='get_products'),
    path('products/add/', addProduct, name='add_product'),

    # Shops
    path('shops/', getShops, name='get_shops'),
    path('shops/add/', addShop, name='add_shop'),

    # Supplier Profiles
    path('supplier-profiles/', getSupplierProfiles, name='get_supplier_profiles'),
    path('supplier-profiles/add/', addSupplierProfile, name='add_supplier_profile'),
]
