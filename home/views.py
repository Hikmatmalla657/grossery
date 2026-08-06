# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import User
from django.contrib import messages
from .forms import UserSignUpForm, LoginForm
from django.contrib.auth.hashers import make_password
from order.models import Order
from django.db.models import Count
from product.models import Product

def login_view(request):
    if request.method == "POST":
        username = request.POST("username")
        password = request.POST("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    form = LoginForm()
    return render(request, "home/login.html", {"form": form})


def Signup_view(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('login')

    else:
        form = UserSignUpForm()
        return render(request, "home/Signup.html", {"form": form})
    
def dashboard_view(request):
    total_users = User.objects.count()
    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    context = {
        "total_users": total_users,
        "total_orders": total_orders,
        "total_products": total_products,
    }
    return render(request, "home/dashboard.html", context)

def logout_view(request):
    logout(request)
    return redirect("login")