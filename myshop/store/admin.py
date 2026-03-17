# store/admin.py
from django.contrib import admin
from .models import Product, CartItem, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')

admin.site.register(CartItem)
admin.site.register(Order)