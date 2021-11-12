from django.db import models
from django.urls import reverse 
from django.contrib import admin
# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=15)
    team = models.BooleanField(default=False)

    def __iter__(self):
        self.a =1
        return self

    def get_absolute_url(self):
        """Returns the url to access a particular game instance."""
        return reverse('player-detail', args=[str(self.id)])

    def get_absolute_url_choose(self):
        return reverse('choose_player', args=[str(self.id)]) 

    def get_absolute_url_score(self):
        return reverse('enter-score', args=[str(self.id)])

    def get_absolute_url_edit(self):
        """Returns the url to access a particular score instance."""
        return reverse('edit-scores-list', args=[str(self.id)])    

    def get_absolute_url_remove(self):
        return reverse('remove-players', args=[str(self.id)])         

    def __str__(self):
        return f'- {self.name} - '