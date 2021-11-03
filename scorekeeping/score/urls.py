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
    path('start/gameplay', views.GamePlay.as_view(), name = 'game-play')
]