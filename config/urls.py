"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('hangman/', include('hangman.urls'))
"""
from django.contrib import admin
from django.urls import path
from hangman.api.hangman import create_game, get_game, update_game

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_game/', create_game),
    path('get_game/<int:id>/', get_game),
    path('update_game/<int:id>/', update_game),
]
