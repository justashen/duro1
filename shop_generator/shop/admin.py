from django.contrib import admin
from .models import Category, Shop, Product, SupplierProfile

admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(SupplierProfile)
