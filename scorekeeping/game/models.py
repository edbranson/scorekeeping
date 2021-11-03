from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib import admin
# Create your models here.

class Game(models.Model):
    description = models.CharField(max_length=20)
    rules_link = models.URLField(max_length=60, default='https://google.com')
    rules_text = models.TextField()

    def get_absolute_url(self):
        """Returns the url to access a particular game instance."""
        return reverse('game-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.description}'