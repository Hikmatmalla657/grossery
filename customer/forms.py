from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Name"}), label="Name")
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Enter Email"}), label="Email")
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Phone Number"}), label="Phone Number", required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Enter Address"}), label="Address")

    class Meta:
        model = Customer
        fields = '__all__'
