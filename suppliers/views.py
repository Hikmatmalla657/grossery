from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from home.mixins import SessionLoginRequiredMixin

from .forms import SupplierForm
from .models import Supplier


class SupplierListView(SessionLoginRequiredMixin, ListView):
    model = Supplier
    template_name = "supplier_list.html"
    context_object_name = "suppliers"


class SupplierCreateView(SessionLoginRequiredMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "add_supplier.html"
    success_url = reverse_lazy("supplier-list")


class SupplierUpdateView(SessionLoginRequiredMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "update_supplier.html"
    success_url = reverse_lazy("supplier-list")


class SupplierDeleteView(SessionLoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = "delete_supplier.html"
    success_url = reverse_lazy("supplier-list")
