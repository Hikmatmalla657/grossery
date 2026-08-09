from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import OrderForm
from .models import Order


class OrderListView(ListView):
    model = Order
    template_name = "orders/order_List.html"
    context_object_name = "orders"
    ordering = ["-order_date", "-order_id"]


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"
    success_url = reverse_lazy("order_list")


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"
    success_url = reverse_lazy("order_list")


class OrderDeleteView(DeleteView):
    model = Order
    template_name = "orders/order_confirm_delete.html"
    success_url = reverse_lazy("order_list")
