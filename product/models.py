from django.db import models


class category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100)

    class Meta:
        db_table = "products"
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def _str_(self):
        return self.name
