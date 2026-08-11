from home.mixins import SessionLoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.shortcuts import render

from .forms import OrderForm
from .models import Order
from django.core.paginator import Paginator

def order_list(request):
    orders = Order.objects.all()
    paginator = Paginator(orders, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'orders/order_list.html', {'orders': page_obj})


class OrderListView(SessionLoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"


class OrderCreateView(SessionLoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"
    success_url = reverse_lazy("orders:order-list")


class OrderUpdateView(SessionLoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"
    success_url = reverse_lazy("orders:order-list")


class OrderDeleteView(SessionLoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy("orders:order-list")
    template_name = "orders/order_confirm_delete.html"
