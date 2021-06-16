from sweets.models import Sweet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# Create your views here.

class SweetList(ListView):
    template_name = 'sweets/list.html'
    model = Sweet


class SweetDetail(DetailView):
    template_name = 'sweets/detail.html'
    model = Sweet
    fields = ['name', 'flavor', 'count', 'purchaser']

class SweetCreate(CreateView):
    template_name = 'sweets/create.html'
    model = Sweet
    fields = ['name', 'flavor', 'count', 'purchaser']

class SweetUpdate(UpdateView):
    template_name = "sweets/update.html"
    model = Sweet
    fields = ['flavor','count']

class SweetDelete(DeleteView):
    template_name = "sweets/delete.html"
    model = Sweet
    success_url = reverse_lazy("list")