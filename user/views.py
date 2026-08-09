from django.shortcuts import render
from django.urls import reverse_lazy
from .models import User
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from home.mixins import SessionLoginRequiredMixin
from .forms import Userform



class UserListView(SessionLoginRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

class UserCreateView(SessionLoginRequiredMixin, CreateView):
    model = User
    form_class = Userform
    template_name = 'add_user.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(SessionLoginRequiredMixin, UpdateView):
    model = User
    form_class = Userform
    template_name = 'update_user.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(SessionLoginRequiredMixin, DeleteView):
    model = User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('user_list')

class UserDetailView(SessionLoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'
