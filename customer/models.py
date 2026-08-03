from django.db import models

# Create your models here.
class customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True,null=True)
    password =models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.TextField(blank=True,null=True)
 #or the id of an existing role object

    

    # windsurf: refactor wxplain
    class Meta:
        db_table = 'customers'
        verbose_name = 'customer'
        verbose_name_plural= 'customers'

        #indsurf: refactor explain genrerate docstring X

        def __str__(self):
            return self.name
        
