from django.http import HttpResponse
from django.views import View


class OrderListView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Order list')


class OrderCreateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Order create')


class OrderUpdateView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Order update')


class OrderDeleteView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Order delete')
