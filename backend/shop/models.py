from django.db import models
from django.contrib.auth.models import User  # Import Django's built-in User model


class Category(models.Model):
    name = models.CharField(max_length=100)
    shop_owner = models.ForeignKey('ShopOwnerProfile', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'shop_owner')  # Ensure unique names per shop owner

    def __str__(self):
        return self.name


class ShopOwnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to User model
    # phone = models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Shop owner profile"


class Shop(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    search = models.TextField(null=True, blank=True)  # Optional field
    address = models.TextField()
    description = models.TextField()
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    tiktok = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    domain_name = models.CharField(max_length=255, unique=True)
    shop_owner = models.ForeignKey(ShopOwnerProfile, on_delete=models.CASCADE)  # Link to ShopOwnerProfile

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    visibility = models.BooleanField(default=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)
    # product_code = models.CharField(max_length=20, unique=True)
    out_of_stock = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/')  # Organized by date
    category = models.ManyToManyField(Category) 
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
