from django.db import models
from django.urls import reverse

from django.contrib import admin
from player.models import Player
from game.models import Game
from play.models import Play


# Create your models here.

class PlaySession(models.Model):
    in_p_playid = models.IntegerField()
    in_p_handid = models.IntegerField(default = 0)
    

class Hand(models.Model):
    hand_num = models.IntegerField()   
    hand_complete = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('play-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.hand_num}, {self.hand_complete}'

class Score(models.Model):
    play = models.ForeignKey(Play, on_delete=models.PROTECT, default="")
    game = models.ForeignKey(Game, on_delete=models.PROTECT, default="")
    player = models.ForeignKey(Player, on_delete=models.PROTECT, default="")
    hand = models.ForeignKey(Hand, on_delete=models.PROTECT, default="")
    amount = models.IntegerField()

    def get_absolute_url(self):
        """Returns the url to access a particular score instance."""
        return reverse('enter-score', args=[str(self.id)])

    def get_absolute_url_update(self):
        """Returns the url to access a particular score instance."""
        return reverse('update-score', args=[str(self.id)])   
        
    def __str__(self):
          return f'{self.id} - {self.amount}'    

class ScoreTotals(models.Model):
    play = models.ForeignKey(Play, on_delete=models.PROTECT, default="")
    player = models.ForeignKey(Player, on_delete=models.PROTECT, default="")
    hand = models.ForeignKey(Hand, on_delete=models.PROTECT, default='')
    hand_total = models.IntegerField(default=0)
    play_total = models.IntegerField(default=0)

    def __str__(self):
          return f'{self.id} - {self.player} - {self.hand_total} - {self.play_total}'