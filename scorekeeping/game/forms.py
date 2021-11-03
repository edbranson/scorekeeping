from django import forms

from django.core.exceptions import ValidationError


class GameCreateForm(forms.Form): 
    description = forms.CharField(max_length=20)
    rules_link = forms.URLField(max_length=40)
    rules_text = forms.CharField(max_length=200)

    def clean_description(self):
        description = self.cleaned_data['description']
        rules_link = self.cleaned_data['rules_link']
        rules_text = self.cleaned_data['rules_text']
        
        # Remember to always return the cleaned data.
        return (description, rules_link, rules_text)
        # return description