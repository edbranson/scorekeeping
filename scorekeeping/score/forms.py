from django import forms

from django.core.exceptions import ValidationError
from .models import Play, Player, Score
from django.forms import ModelMultipleChoiceField


class ChoosePlayersForm(forms.Form):
    players = forms.ModelMultipleChoiceField(queryset=Player.objects.all(), to_field_name='id', label="Choose Players", widget= forms.CheckboxSelectMultiple)

    def clean_description(self):
        players = self.cleaned_data['players']
        return (players.id)

class GamePlayForm(forms.Form):
    
    def clean_description(self):
        self.play_id_selected = play_id_selected
        return (self.play_id_selected)

class EnterScoreForm(forms.Form):
    amt = forms.IntegerField()
   
    def clean_description(self):
        amt = self.cleaned_data['amt']
        
        # Remember to always return the cleaned data.
        return (amt)


class UpdateScoreForm(forms.Form):
    edit_amt = forms.IntegerField()

    def clean_description(self):
        amt = self.cleaned_data['edit_amt']
        # Remember to always return the cleaned data.
        return (edit_amt)        

class RemovePlayersForm(forms.Form):

    def clean_description(self):
        players = self.cleaned_data['player']
        return (player.id)

class GameCompleteForm(forms.Form):
    completed = forms.BooleanField()

    def clean_description(self):
        competed = self.cleaned_data['completed'] 
        return (completed)       