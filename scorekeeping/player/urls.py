"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib import admin
from django.urls import include
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    path('player/', views.PlayerListView.as_view(), name='player-list'),
    path('player/<int:pk>', views.PlayerDetailView.as_view(), name='player-detail'),
    path('player/create/', views.PlayerCreate.as_view(), name='player-create'),
    path('player/<int:pk>/update/', views.PlayerUpdate.as_view(), name='player-update'),
    path('player/<int:pk>/delete/', views.PlayerDelete.as_view(), name='player-delete'),
]