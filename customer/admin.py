
# Register your models here.
from django.contrib import admin
from .models import customer


# Register your models here.

@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'created_at', 'updated_at')
    search_fields = ('name', 'email','phone')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    

  

