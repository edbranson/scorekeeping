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
    path('play/', views.PlayListView.as_view(), name='play-list'),
    path('play/archive', views.PlayArchiveListView.as_view(), name='play-archive-list'),
    path('play/<int:pk>', views.PlayDetailView.as_view(), name='play-detail'),
    path('play/create', views.PlayCreate.as_view(), name='play-create'),
    path('play/<int:pk>/update/', views.PlayUpdate.as_view(), name='play-update'),
    path('play/<int:pk>/delete/', views.PlayDelete.as_view(), name='play-delete')   
]
