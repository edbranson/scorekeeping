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


# def game_create(request):
#     game = Game()
#     # Create a form instance and populate it with data from the request (binding):
#     if request.method == 'POST':
#         # Create a form instance and populate it with data from the request (binding):
#         form = GameCreateForm(request.POST)
#     # Check if the form is valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required (here we just write it to the model description field)
#             game.description = form.cleaned_data['description']
#             game.rules_text = form.cleaned_data['rules_text']
#             game.save()
#             return HttpResponseRedirect(reverse('game-list'))
#     else:
#         proposed_description = ""
#         form = GameCreateForm(initial={'description': "", 'rules_text': ""})
#         # form = GameCreateForm(initial={'description': "", 'rules_link':"gmcpas.com", 'rules_text': ""})
#     context = {'form': form, }
#     return render(request, 'game_form.html', context)


# def game_update(request, pk):
#     game = get_object_or_404(Game, pk=pk)
#     # Create a form instance and populate it with data from the request (binding):
#     if request.method == 'POST':
#         # Create a form instance and populate it with data from the request (binding):
#         form = GameCreateForm(request.POST)
#     # Check if the form is valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required (here we just write it to the model description field)
#             game.description = form.cleaned_data['description']
#             game.save()
#             return HttpResponseRedirect(reverse('game-list'))
#     else:
#         proposed_description = game.description
#         form = GameCreateForm(initial={'description': proposed_description})
#     context = {'form': form, }
#     return render(request, 'game_form.html', context)

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
