from django import forms
from customer.models import Customer
from product.models import Product
from .models import Order


class OrderForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), label='Customer')
    order_date = forms.DateField(widget=forms.DateInput(attrs={"placeholder": "Enter Order Date"}), label='Order Date')
    status = forms.ChoiceField(choices=Order.OrderStatus.choices, label='Status')
    order_details = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), label='Order Details')

    class Meta:
        model = Order
        fields = '__all__'
