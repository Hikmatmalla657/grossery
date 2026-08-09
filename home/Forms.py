from django import forms
from user.models import User, Role


class UserSignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ["name", "email", "password", "phone", "address", "role"]
        widgets = {
            "password": forms.PasswordInput(attrs={"placeholder": "Enter Password"})
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match!")

        return cleaned_data


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter Email"}),
        label="Email"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter Password"}),
        label="Password"
    )