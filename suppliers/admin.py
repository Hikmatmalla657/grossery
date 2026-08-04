from django.contrib import admin
from .models import Supplier

# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
   list_display = ('name', 'email', 'phone', 'created_at', 'updated_at',)
   search_fields = ('name', 'email','phone')
   list_filter = ('created_at', 'updated_at')
   readonly_fields = ('created_at', 'updated_at')

