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


# urlpatterns = [
#     path('admin/', admin.site.urls),
# ] 

urlpatterns = [
    path('home/', views.index, name='index'),
    path('game/', views.GameListView.as_view(), name='game-list'),
    path('game/<int:pk>', views.GameDetailView.as_view(), name='game-detail'),
    path('game/create', views.GameCreate.as_view(), name='game-create'),
    path('game/<int:pk>/update/', views.GameUpdate.as_view(), name='game-update'),
    path('game/<int:pk>/delete/', views.GameDelete.as_view(), name='game-delete'),
    
]

# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]