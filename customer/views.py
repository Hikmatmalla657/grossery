from home.mixins import SessionLoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CustomerForm
from .models import Customer


class CustomerListView(SessionLoginRequiredMixin, ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'customer_list.html'


class CustomerCreateView(SessionLoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'add_customer.html'
    success_url = reverse_lazy('customer-list')


class CustomerUpdateView(SessionLoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'update_customer.html'
    success_url = reverse_lazy('customer-list')


class CustomerDeleteView(SessionLoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'delete_customer.html'
    success_url = reverse_lazy('customer-list')
