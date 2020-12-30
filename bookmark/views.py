from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import bookmark


class bookmarkListView(ListView):
    model = bookmark

class bookmarkCreateView(CreateView):
    model = bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class bookmarkDetailView(DetailView):
    model = bookmark

class bookmarkUpdateView(UpdateView):
    model = bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class bookmarkDeleteView(DeleteView):
    model = bookmark
    success_url = reverse_lazy('list')