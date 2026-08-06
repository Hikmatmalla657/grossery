from django import forms
from .models import Supplier


class SupplierForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Supplier Name"}), label='Name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Enter Email"}), label='Email')
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Phone"}), label='Phone')
    address = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Enter Address"}), label='Address')

    class Meta:
        model = Supplier
        fields = '__all__'
