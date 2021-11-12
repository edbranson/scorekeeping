#from django.http import HttpResponse
# Create your views here.
from .models import Game
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from game.forms import GameCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
# def index(request, game_description):

def index(request):
    return render(request, 'index.html',)

class GameListView(generic.ListView):
    model = Game

class GameDetailView(generic.DetailView):
    model = Game

class GameCreate(generic.CreateView):
    model = Game
    fields = ['description', 'rules_link', 'rules_text']

class GameUpdate(generic.UpdateView):
    model = Game
    fields = ['description', 'rules_link', 'rules_text']

class GameDelete(generic.DeleteView):
    model = Game
    success_url = reverse_lazy('game-list')
