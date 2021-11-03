from django.shortcuts import get_object_or_404, render

from django.shortcuts import render
from .models import Player

from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class PlayerListView(generic.ListView):
    model = Player
    
class PlayerDetailView(generic.DetailView):
    model = Player   

class PlayerCreate(generic.CreateView):
    model = Player
    fields = ['name', 'team']   

class PlayerUpdate(generic.UpdateView):
    model = Player
    fields = ['name', 'team']    

class PlayerDelete(generic.DeleteView):
    model = Player
    success_url = reverse_lazy('player-list')       