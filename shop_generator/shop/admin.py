from django.contrib import admin
from .models import Category, Shop, Product, ShopOwnerProfile

admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(ShopOwnerProfile)
