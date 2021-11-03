from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib import admin
# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=15)
    team = models.BooleanField(default=False)

    def get_absolute_url(self):
        """Returns the url to access a particular game instance."""
        return reverse('player-detail', args=[str(self.id)])

    def get_absolute_url_choose(self):
        return reverse('choose_player', args=[str(self.id)])    

    def __str__(self):
        return f'{self.id} - {self.name} - {self.team}'