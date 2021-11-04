from django.db import models

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
        return reverse('score-detail', args=[str(self.id)])

     def __str__(self):
          return f'{self.id} - {self.amount}'    


# class MMPlayer(models.Model):   
#     players = models.ManyToManyField('player.Player', through="PlayPlayer", through_fields=('mmplayer', 'player'))

#     def __str__(self):
#         return f'{self.id} - {self.players.name}'


# class MMHand(models.Model):
#     hands = models.ManyToManyField('Hand', through="PlayHand", through_fields=('mmhand', 'hand')) 

# class PlayHand(models.Model):
#     mmhand = models.ForeignKey(MMHand, on_delete=models.PROTECT, default ="", null=True, blank=True)
#     hand = models.ForeignKey(Hand, on_delete=models.PROTECT, default ="", null=True, blank=True)

#     # def __str__(self):
#     #             return f' MMHandr id: {self.mmhand.id} - Hand#: {self.hand.hand_num}' 

# class PlayPlayer(models.Model):
#     player = models.ForeignKey('player.Player', on_delete=models.PROTECT, default ="", null=True, blank=True)
#     mmplayer = models.ForeignKey(MMPlayer, on_delete=models.PROTECT, default ="", null=True, blank=True)    

#     # def __str__(self):
#     #         return f' MMPlayer id: {self.mmplayer.id} - Player: {self.player.name}'    