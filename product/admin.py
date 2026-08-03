from django.contrib import admin
from .models import Product, category


# Register your models here.

@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
 list_display = ('id', 'name', 'created_at', 'expiry_date')
 search_fields = ('name',)
 list_filter = ('created_at', 'expiry_date')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)