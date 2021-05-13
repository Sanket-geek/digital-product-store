from django.contrib import admin
from django.contrib.auth.models import User
from .models import Product, Payment, UserProduct, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(UserProduct)