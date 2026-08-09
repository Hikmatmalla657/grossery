from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from home.mixins import SessionLoginRequiredMixin

from .forms import ProductForm
from .models import Product


class ProductListView(SessionLoginRequiredMixin, ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"


class ProductCreateView(SessionLoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "add_product.html"
    success_url = reverse_lazy("product-list")


class ProductUpdateView(SessionLoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "update_product.html"
    success_url = reverse_lazy("product-list")


class ProductDeleteView(SessionLoginRequiredMixin, DeleteView):
    model = Product
    template_name = "delete_product.html"
    success_url = reverse_lazy("product-list")
