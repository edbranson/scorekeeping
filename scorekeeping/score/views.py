
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Play, Game, Hand, Score, Player
from play.forms import PlayCreateForm
from score.forms import ChoosePlayersForm, GamePlayForm
from datetime import datetime
from datetime import date
from django.db import models

# Create your views here.

class PlaySelect(View):
    
    def get(self, request, pk):
        global play_in_progress 
        play_in_progress = get_object_or_404(Play, pk=pk)
        
        context = {'game_desc': play_in_progress.game.description, 'play_date': play_in_progress.play_date, 'location': play_in_progress.location,
        'play_id_selected': play_in_progress.id}    
        return render(request, 'score/game_selected.html', context)  


class GamePlay(View):
     
    def get(self, request):
        # form = GamePlayForm()
        context = {'game_desc': play_in_progress.game.description, 'play_date': play_in_progress.play_date,
         'location': play_in_progress.location, 'play_id_selected': play_in_progress.id}      
        return render(request, 'score/game_play.html', context)
    #    , 'hand': hand_filter.hand_num

class StartPlay(generic.ListView):
    model = Play
    context_object_name = 'start_play'
    queryset = Play.objects.filter(play_complete = False)
    template_name = 'score/start_play.html'

class ChoosePlayers(View):
   
    def post(self, request):      
        # Create a form instance and populate it with data from the request (binding):
        form = ChoosePlayersForm(request.POST) 
        
        if form.is_valid():
            players_selected = form.cleaned_data['players']
            # process the data in form.cleaned_data as required (here we just write it to the model location field)
            if not play_in_progress.hands.all(): 
                hand = Hand.objects.create(hand_num = 1)
                play_in_progress.hands.add(hand)
                print(play_in_progress.hands.all())

            for x in players_selected:
                play_in_progress.players.add(x)
                print(play_in_progress.players.all())
            context = {'game_desc': play_in_progress.game.description, 'play_date': play_in_progress.play_date,
            'location': play_in_progress.location, 'play_id_selected': play_in_progress.id}  
            return HttpResponseRedirect(reverse('game-play'))
        else:
            form = ChoosePlayersForm()

        context = {'form':form, 'game_desc': play_in_progress.game.description, 'play_date': play_in_progress.play_date,
         'location': play_in_progress.location, 'play_id_selected': play_in_progress.id}    
        return render(request, 'score/choose_players.html', context)  
    
    def get(self, request):
        # play = get_object_or_404(Play, pk=pk) 
        form = ChoosePlayersForm()
        context = {'form':form, 'game_desc': play_in_progress.game.description, 'play_date': play_in_progress.play_date,
         'location': play_in_progress.location, 'play_id_selected': play_in_progress.id}    
        return render(request, 'score/choose_players.html', context)  



