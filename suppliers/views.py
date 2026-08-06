from django.http import HttpResponse
from django.views import View


class SupplierListView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Supplier list')


class SupplierCreateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Supplier create')


class SupplierUpdateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Supplier update')


class SupplierDeleteView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Supplier delete')
