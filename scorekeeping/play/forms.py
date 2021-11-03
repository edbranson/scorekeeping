from django import forms

from django.core.exceptions import ValidationError
from .models import Game
from datetime import datetime
from datetime import date
from django.forms import ModelChoiceField


class PlayCreateForm(forms.Form):
    play_today = date.today()
    game = forms.ModelChoiceField(queryset=Game.objects.all(), to_field_name='id', label="Choose Game")
    location = forms.CharField(max_length=30)
    play_date = forms.DateField()
    # play_date = forms.DateField(initial=datetime(2000,1,1).date())
    play_complete = forms.BooleanField(required=False)

    def clean_description(self):
        location = self.cleaned_data['location']
        game = self.cleaned_data['game']
        play_date = self.cleaned_data['play_date']
        play_complete = self.cleaned_data['play_complete']
        # Remember to always return the cleaned data.
        return (location, game, play_date, play_complete)

class PlayUpdateForm(forms.Form):
    game = forms.ModelChoiceField(queryset=Game.objects.all(), label="Choose Game", to_field_name='id')
    game_desc = forms.CharField(max_length= 20)
    location = forms.CharField(max_length=30)
    play_date = forms.DateField()
    play_complete = forms.BooleanField(required=False)

    def clean_description(self):
        location = self.cleaned_data['location']
        game = self.cleaned_data['game']
        game_desc = self.cleaned_data['game_desc']
        play_date = self.cleaned_data['play_date']
        play_complete = self.cleaned_data['play_complete']
        # Remember to always return the cleaned data.
        return (game_desc, location, game, play_date, play_complete)        