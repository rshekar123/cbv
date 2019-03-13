from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from .models import shekar
from django.urls import reverse_lazy
# Create your views here.


class shekarListView(ListView):
    model = shekar
    context_object_name = 'shekar'

class shekardetailview(DetailView):
    model = shekar

class shekarcreateview(CreateView):
    model = shekar
    fields = ('name','age','salary')

class shekarupdateview(UpdateView):
    model = shekar
    fields = ('name','age','salary')

class deleteview(DeleteView):
    model = shekar
    success_url=reverse_lazy('list')