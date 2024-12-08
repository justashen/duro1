from django.contrib import admin
from .models import Category, Shop, Product, ShopOwnerProfile

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(ShopOwnerProfile)
