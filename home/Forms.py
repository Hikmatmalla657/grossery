from user.models import User, Role
from django import forms


class UserRegisterform(forms.modelForm):
    confirm_password = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder": "confirm_password"}), label="confirm_data")

    class Meta:
        model = User
        fileds = ["name", "email", "password", "phone", "address", "confirm_password", "role"]
        widgets = {"password": forms.PasswordInput(attrs={"placeholder": "enter password"})},


def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get("password")
    confirm_password = cleaned_data.get("confirm_password")

    if password and confirm_password and password != confirm_password:
        self.add_error(confirm_password, "password do not match!")

        return cleaned_data


class UserLoginform(forms.model.form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "enter email"}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "enter password"}), label ="password")
    confirm_password = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder": "confirm_password"}), label="confirm_data")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "passwords do not match!")

        return cleaned_data
    
   