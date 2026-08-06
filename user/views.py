from django.shortcuts import render
from .models import User
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Userform



class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'

class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = Userform
    template_name = 'user/user_form.html'
    success_url = '/users/'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = Userform
   # template_name = 'user/user_form.html'
    success_url = '/users/'

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'user/user_confirm_delete.html'
    success_url = '/users/'

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'