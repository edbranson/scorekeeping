from django import forms

from django.core.exceptions import ValidationError
from .models import Play, Player
from django.forms import ModelMultipleChoiceField


class ChoosePlayersForm(forms.Form):
    # play_id_selected = forms.IntegerField(widget = forms.HiddenInput())
    players = forms.ModelMultipleChoiceField(queryset=Player.objects.all(), to_field_name='id', label="Choose Players")

    def clean_description(self):
        players = self.cleaned_data['players']
        return (players.id)

class GamePlayForm(forms.Form):
    
    def clean_description(self,):
        self.play_id_selected = play_id_selected
        return (self.play_id_selected)