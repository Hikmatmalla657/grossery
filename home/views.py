from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import UserLoginForm, UserSignUpForm
from user.models import User
from orders.models import Order
from product.models import Product


def login_view(request):
    form = UserLoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.filter(email=email).first()

            if user and check_password(password, user.password):
                request.session["user_id"] = user.pk
                request.session["user_name"] = user.name
                next_url = request.POST.get("next") or request.GET.get("next")
                if next_url and url_has_allowed_host_and_scheme(
                    next_url, allowed_hosts={request.get_host()}
                ):
                    return redirect(next_url)
                return redirect("dashboard")

            messages.error(request, "Invalid email or password.")

    return render(request, "home/login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data["password"])
            user.save()

            messages.success(request, "Account created successfully. You can now log in.")
            return redirect("login")
    else:
        form = UserSignUpForm()

    return render(request, "home/signup.html", {"form": form})


def dashboard_view(request):
    total_users = User.objects.count()
    total_orders = Order.objects.count()
    total_products = Product.objects.count()

    # Order status counts for dashboard summary
    status_count = {
        "pending": Order.objects.filter(status=Order.OrderStatus.PENDING).count(),
        "processing": Order.objects.filter(status=Order.OrderStatus.PROCESSING).count(),
        "shipped": Order.objects.filter(status=Order.OrderStatus.SHIPPED).count(),
        "delivered": Order.objects.filter(status=Order.OrderStatus.DELIVERED).count(),
        "cancelled": Order.objects.filter(status=Order.OrderStatus.CANCELLED).count(),
    }

    context = {
        "total_users": total_users,
        "total_orders": total_orders,
        "total_products": total_products,
        "status_count": status_count,
    }

    return render(request, "home/dashboard.html", context)


def logout_view(request):
    request.session.flush()
    return redirect("login")
