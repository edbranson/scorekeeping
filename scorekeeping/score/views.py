
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Play, Game, Hand, Score, Player, PlaySession
from play.forms import PlayCreateForm
from score.forms import ChoosePlayersForm, GamePlayForm
from datetime import datetime
from datetime import date
from django.db import models

# Create your views here.

class PlaySelect(View):
    
    def get(self, request, pk):
        # global play_in_progress 
        play_in_progress = get_object_or_404(Play, pk=pk)
        try:
            ipid = get_object_or_404(PlaySession)
        except:
            ipid = PlaySession.objects.create(in_p_playid = play_in_progress.id)
        else:    
            ipid = PlaySession.objects.get(pk=1)
            ipid.in_p_playid = play_in_progress.id
            ipid.save()

        context = {'game_desc': play_in_progress.game.description, 'play_date': play_in_progress.play_date, 'location': play_in_progress.location,
        'play_id_selected': play_in_progress.id}    
        return render(request, 'score/game_selected.html', context)  


class GamePlay(View):
    
    def get(self, request):
        # Get play in progress Play object useing PlaySession in_p_playid field
        ipid = get_object_or_404(PlaySession, pk=1)  
        play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)
        hand_number = get_object_or_404(Hand, pk=ipid.in_p_handid)

        context = {'game_desc': play_in_progress.game.description, 'play_date': play_in_progress.play_date,
         'location': play_in_progress.location, 'play_id_selected': play_in_progress.id, 'hand': hand_number.hand_num,
         'players': play_in_progress.players.all()}      
        return render(request, 'score/game_play.html', context)
  
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
            # Get play in progress Play object useing PlaySession in_p_playid field
            ipid = get_object_or_404(PlaySession, pk=1)  
            play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)

            # process the data in form.cleaned_data as required (here we just write it to the model location field)
            players_selected = form.cleaned_data['players']
            
            #create or update the hand instance of the play database
            if not play_in_progress.hands.all(): 
                hand = Hand.objects.create(hand_num = 1)
                play_in_progress.hands.add(hand)

            
            #expecting only one "active" hand in the Play database
            query = play_in_progress.hands.get(hand_complete = False)
            #store the active "Hand" in the PlaySession database record
            ipid.in_p_handid = query.pk 
            ipid.save()

            #post the players selected to the current "Play" play in progress record via a many to many field
            for x in players_selected:
                play_in_progress.players.add(x)
            return HttpResponseRedirect(reverse('game-play'), headers={'players': play_in_progress.players.all()})
        else:
            form = ChoosePlayersForm()   
        return render(request, 'score/choose_players.html', context)  
    
    def get(self, request):
        # Get play in progress Play object useing PlaySession in_p_playid field
        ipid = get_object_or_404(PlaySession, pk=1)  
        play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)
        form = ChoosePlayersForm()
        context = {'form':form, 'game_desc': play_in_progress.game.description, 'play_date': play_in_progress.play_date,
         'location': play_in_progress.location, 'play_id_selected': play_in_progress.id, 'hand': play_in_progress.hands.all()}    
        return render(request, 'score/choose_players.html', context)  



