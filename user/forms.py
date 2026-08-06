from django import forms
from .models import User

class Userform(forms.ModelForm):
    name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"enter Name"}), label= "Name",)
    Email = forms.EmailField(widget= forms.EmailInput(attrs={"placeholder":"enter Email"}), label= "Email",)
    password = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder":"enter Password"}), label= "Password",)

    class Meta:
        model = User
        fields = '__all__'
        