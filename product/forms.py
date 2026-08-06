from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Product Name"}), label='Name')
    price = forms.DecimalField(widget=forms.NumberInput(attrs={"placeholder": "Enter Price"}), label='Price')
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Enter Quantity"}), label='Quantity')
    category = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Category"}), label='Category')

    class Meta:
        model = Product
        fields = '__all__'
