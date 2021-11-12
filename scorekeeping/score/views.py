
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Play, Game, Hand, Score, Player, PlaySession, ScoreTotals
from play.forms import PlayCreateForm
from score.forms import ChoosePlayersForm, EnterScoreForm, RemovePlayersForm, GamePlayForm, UpdateScoreForm, GameCompleteForm
from datetime import datetime
from datetime import date
from django.db import models
from django.db.models import Sum

# Create your views here.

class EnterScore(View):
    
    def post(self, request, pk):
        score = Score()

        # Create a form instance and populate it with data from the request (binding):
        form = EnterScoreForm(request.POST)
        player = get_object_or_404(Player, pk=pk)
        ipid = get_object_or_404(PlaySession, pk=1)  
        play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)
        hand_number = get_object_or_404(Hand, pk=ipid.in_p_handid) 
        
        if form.is_valid():
        
            # process the data in form.cleaned_data as required (here we just write it to the model location field)
            score.game = play_in_progress.game
            score.play = play_in_progress
            score.player = player
            score.hand = hand_number
            score.amount = form.cleaned_data['amt']
            score.save()

            # query for 'the' play/player/hand record in Model ScoreTotals.  Only one record by design below.
            q_player_hand = ScoreTotals.objects.filter(play=play_in_progress.id, hand=hand_number, player = player)
            # get the sum of play/player/hand scores .. totals for this hand
            q_hand_sum = Score.objects.filter(play=play_in_progress.id, hand=hand_number, player = player).aggregate(hand_sum=Sum('amount'))
            # get the sum of play/player scores .. totals for this play
            q_play_sum = Score.objects.filter(play=play_in_progress.id, player = player).aggregate(play_tot=Sum('amount'))

            # create of update the play/player and play/player/hand totals record in ScoreTotals model.
            if q_hand_sum['hand_sum']:
                if q_player_hand:
                    q_player_hand[0].hand_total = q_hand_sum['hand_sum']
                    q_player_hand[0].play_total = q_play_sum['play_tot']
                    q_player_hand[0].save()
                else:    
                    hand_sum = ScoreTotals.objects.create(player = player, hand = hand_number, play = play_in_progress, hand_total = q_hand_sum['hand_sum'],
                    play_total = q_play_sum['play_tot'])

            return HttpResponseRedirect(reverse('game-play') )

    def get(self, request, pk):
        score = Score()
        player = get_object_or_404(Player, pk=pk)
        ipid = get_object_or_404(PlaySession, pk=1)  
        play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)
        hand_number = get_object_or_404(Hand, pk=ipid.in_p_handid)
        # queryset of play/player/scores
        q_player_score = Score.objects.filter(play=play_in_progress.id, player = player)
        scores = q_player_score

        form = EnterScoreForm()
        context = {'form':form, 'player': player, 'scores': scores}
        return render(request, 'score/enter_score.html', context)


class UpdateScore(View):

    def post(self, request, pk):
        score = get_object_or_404(Score, pk=pk)   
        player = score.player
           
        # Create a form instance and populate it with data from the request (binding):
        form = UpdateScoreForm(request.POST) 
        ipid = get_object_or_404(PlaySession, pk=1)  
        play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)
        hand_number = get_object_or_404(Hand, pk=ipid.in_p_handid) 
        
        if form.is_valid():
            score.amount = form.cleaned_data['edit_amt']
            score.save()

            # query for 'the' play/player/hand record in Model ScoreTotals.  Only one record by design below.
            q_player_hand = ScoreTotals.objects.filter(play=play_in_progress.id, hand=hand_number, player = player)
            # get the sum of play/player/hand scores .. totals for this hand
            q_hand_sum = Score.objects.filter(play=play_in_progress.id, hand=hand_number, player = player).aggregate(hand_sum=Sum('amount'))
            # get the sum of play/player scores .. totals for this play
            q_play_sum = Score.objects.filter(play=play_in_progress.id, player = player).aggregate(play_tot=Sum('amount'))

            # create of update the play/player and play/player/hand totals record in ScoreTotals model.
            if q_hand_sum['hand_sum']:
                if q_player_hand:
                    q_player_hand[0].hand_total = q_hand_sum['hand_sum']
                    q_player_hand[0].play_total = q_play_sum['play_tot']
                    q_player_hand[0].save()
                else:    
                    hand_sum = ScoreTotals.objects.create(player = player, hand = hand_number, play = play_in_progress, hand_total = q_hand_sum['hand_sum'],
                    play_total = q_play_sum['play_tot'])

            return HttpResponseRedirect(reverse('game-play') )

    def get(self, request, pk):
        
        score = get_object_or_404(Score, pk=pk)
        player = score.player
       
        ipid = get_object_or_404(PlaySession, pk=1)  
        play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)
        # hand_number = get_object_or_404(Hand, pk=ipid.in_p_handid)
        # # queryset of play/player/scores
        q_player_score = Score.objects.filter(play=play_in_progress.id, player = player)
       
        form = UpdateScoreForm(initial={'edit_amt': score.amount})

        context = {'form': form, 'player': player, 'score': score}
        return render(request, 'score/update_score.html', context)  

class EditScoresList(View):

    def post(self, request, pk):
        # score = get_object_or_404(Score, pk=pk)
        player = get_object_or_404(Player, pk=pk)
        ipid = get_object_or_404(PlaySession, pk=1)  
        play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)
        hand_number = get_object_or_404(Hand, pk=ipid.in_p_handid) 

        if form.is_valid():
            form = UpdateScoreForm(request.POST)
            score.amount = form.cleaned_data['edit_amt']
            score.save()

        return HttpResponseRedirect(reverse('edit-scores-list') )
        

    def get(self, request, pk):
        player = get_object_or_404(Player, pk=pk)
        # score = get_object_or_404(Score, pk=pk)
        ipid = get_object_or_404(PlaySession, pk=1)  
        play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)
        hand_number = get_object_or_404(Hand, pk=ipid.in_p_handid) 
        q_player_score = Score.objects.filter(play=play_in_progress.id, player = player)
        form = UpdateScoreForm()

        context = {'form':form, 'player': player, 'scores': q_player_score}
        return render(request, 'score/edit_scores_list.html', context)  
         

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
        'play_id_selected': play_in_progress.id, 'play': play_in_progress}    
        return render(request, 'score/game_selected.html', context)  


class GamePlay(View):
   
    def get(self, request):
        # Get play in progress Play object useing PlaySession in_p_playid field
        ipid = get_object_or_404(PlaySession, pk=1)  
        play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)
        hand_number = get_object_or_404(Hand, pk=ipid.in_p_handid)
        summary = ScoreTotals.objects.filter(play = play_in_progress.id, hand = hand_number)
        players = play_in_progress.players.all()

        for player in players:
        # query for 'the' play/player/hand record in Model ScoreTotals.  Only one record by design below.
            q_player_hand = ScoreTotals.objects.filter(play=play_in_progress.id, hand=hand_number, player = player)
            # get the sum of play/player/hand scores .. totals for this hand
            q_hand_sum = Score.objects.filter(play=play_in_progress.id, hand=hand_number, player = player).aggregate(hand_sum=Sum('amount'))
            # get the sum of play/player scores .. totals for this play
            q_play_sum = Score.objects.filter(play=play_in_progress.id, player = player).aggregate(play_tot=Sum('amount'))
           
            # create of update the play/player and play/player/hand totals record in ScoreTotals model.
            if q_hand_sum['hand_sum'] != None:
                if q_player_hand:
                    q_player_hand[0].hand_total = q_hand_sum['hand_sum']
                    q_player_hand[0].play_total = q_play_sum['play_tot']
                    q_player_hand[0].save()
                else:    
                    hand_sum = ScoreTotals.objects.create(player = player, hand = hand_number, play = play_in_progress, hand_total = q_hand_sum['hand_sum'],
                    play_total = q_play_sum['play_tot'])
       
        context = { 'hand': hand_number, 'players': play_in_progress.players.all(), 'summary': summary, 'play': play_in_progress}      
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

        #create or update the hand instance of the play database
        if not play_in_progress.hands.all(): 
            hand = Hand.objects.create(hand_num = 1)
            play_in_progress.hands.add(hand)
        #expecting only one "active" hand in the Play database
        query = play_in_progress.hands.get(hand_complete = False)
        #store the active "Hand" in the PlaySession database record
        ipid.in_p_handid = query.pk 
        ipid.save()

        form = ChoosePlayersForm()
        context = {'form':form, 'play': play_in_progress, 'game_desc': play_in_progress.game.description, 'play_date': play_in_progress.play_date,
         'location': play_in_progress.location, 'play_id_selected': play_in_progress.id, 'hand': play_in_progress.hands.all(), 'players': play_in_progress.players.all()}    
        return render(request, 'score/choose_players.html', context)  

class RemovePlayers(View):
    score = Score()

    def post(self, request, pk):
        form = RemovePlayersForm(request.POST) 
        if form.is_valid():
            player = get_object_or_404(Player, pk=pk)
            ipid = get_object_or_404(PlaySession, pk=1)  
            play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)
            play_in_progress.players.remove(player)
            return HttpResponseRedirect(reverse('game-play') )

    def get(self, request, pk):
        player = get_object_or_404(Player, pk=pk)
        ipid = get_object_or_404(PlaySession, pk=1)  
        play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)
        query = Score.objects.filter(play=play_in_progress.id, player = player)
        if query:
            can_remove = False
        else:
            can_remove = True
        form = RemovePlayersForm()
        context = {'form': form, 'player': player, 'can_remove': can_remove}
        return render(request, 'score/remove_players_confirm.html', context)


class HandComplete(View):

    def get(self,request):
        ipid = get_object_or_404(PlaySession, pk=1)  
        play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)
        hand = get_object_or_404(Hand, pk=ipid.in_p_handid)
        num = hand.hand_num
        num += 1
       
        hand.hand_complete = True
        hand.save()
        hand = Hand.objects.create(hand_num = num,)
        play_in_progress.hands.add(hand)
        ipid.in_p_handid = hand.id
        ipid.save()
        for player in play_in_progress.players.all():
             # query for 'the' play/player/hand record in Model ScoreTotals.  Only one record by design below.
            q_player_hand = ScoreTotals.objects.filter(play=play_in_progress.id, hand=hand, player = player)
            # get the sum of play/player/hand scores .. totals for this hand
            q_hand_sum = Score.objects.filter(play=play_in_progress.id, hand=hand, player = player).aggregate(hand_sum=Sum('amount'))
            # get the sum of play/player scores .. totals for this play
            q_play_sum = Score.objects.filter(play=play_in_progress.id, player = player).aggregate(play_tot=Sum('amount'))
            # create of update the play/player and play/player/hand totals record in ScoreTotals model.
            if q_play_sum['play_tot']:
                hand_sum = ScoreTotals.objects.create(player = player, hand = hand, play = play_in_progress, play_total = q_play_sum['play_tot'])
                
        summary = ScoreTotals.objects.filter(play = play_in_progress.id, hand = hand)
        context = {'hand': hand,'players': play_in_progress.players.all(), 'summary': summary, 'play': play_in_progress}
        
        return HttpResponseRedirect(reverse('game-play'))
       

class GameComplete(View):
    def post(self, request):      
        # Create a form instance and populate it with data from the request (binding):
        form = GameCompleteForm(request.POST) 
        
        if form.is_valid():
            # Get play in progress Play object useing PlaySession in_p_playid field
            ipid = get_object_or_404(PlaySession, pk=1)  
            play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)

            # process the data in form.cleaned_data as required (here we just write it to the model location field)
            completed = form.cleaned_data['completed']
            
            play_in_progress.play_complete = completed
            play_in_progress.save()

            return HttpResponseRedirect(reverse('start-play'))
        else:
            form = GameCompleteForm()   
        return render(request, 'score/game_complete.html', context)  
        
    def get(self, request):
        # Get play in progress Play object useing PlaySession in_p_playid field
        ipid = get_object_or_404(PlaySession, pk=1)  
        play_in_progress = get_object_or_404(Play, pk=ipid.in_p_playid)
        
        form = GameCompleteForm()
        context = {'form':form, 'completed':play_in_progress.play_complete}    
        return render(request, 'score/game_complete.html', context)  

        
