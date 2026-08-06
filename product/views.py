from django.http import HttpResponse
from django.views import View


class ProductListView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Product list')


class ProductCreateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Product create')


class ProductUpdateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Product update')


class ProductDeleteView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Product delete')
