from django.urls import path
from django.contrib import admin
from django.urls import include
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('start/', views.StartPlay.as_view(), name='start-play'),
    path('start/<int:pk>', views.PlaySelect.as_view(), name='play-select'),
    path('start/chooseplayers', views.ChoosePlayers.as_view(), name='choose-players'),
    path('start/gameplay', views.GamePlay.as_view(), name = 'game-play'),
    path('start/enterscore/<int:pk>', views.EnterScore.as_view(), name = 'enter-score'),
    path('start/player/<int:pk>/remove/', views.RemovePlayers.as_view(), name='remove-players'),
    path('start/gameplay/hand', views.HandComplete.as_view(), name = 'hand-complete'),
    path('start/enterscore/<int:pk>/edit', views.EditScoresList.as_view(), name = 'edit-scores-list'),
    path('start/enterscore/<int:pk>/update', views.UpdateScore.as_view(), name = 'update-score'),
    path('start/complete', views.GameComplete.as_view(), name = 'game-complete')
]