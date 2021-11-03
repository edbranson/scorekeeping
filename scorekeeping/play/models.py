from django.db import models
from datetime import datetime
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib import admin
from game.models import Game
from player.models import Player
# from play.models import Play
# Create your models here.

class Play(models.Model):
    game = models.ForeignKey('game.Game', on_delete=models.RESTRICT)
    players = models.ManyToManyField('player.Player')
    hands = models.ManyToManyField('score.Hand')
    # playplayer = models.ForeignKey('score.PlayPlayer', on_delete=models.RESTRICT, default="", null=True, blank=True)
    # playhand = models.ForeignKey('score.PlayHand', on_delete=models.RESTRICT, default="", null=True, blank=True)
    play_date = models.DateField(auto_now=False, default ='2021-10-20')
    location = models.CharField(max_length=30)
    play_complete = models.BooleanField(default=False)

    def get_absolute_url(self):
        """Returns the url to access a particular Play instance."""
        return reverse('play-detail', args=[str(self.id)])

    def get_absolute_url_start(self):
        return reverse('play-select', args=[str(self.id)])

    def get_absolute_url_choose(self):
        return reverse('choose-player', args=[str(self.id)])          

    def __str__(self):
        return f'{self.game.description},  {self.play_date},  {self.location},  {self.play_complete}'


