from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<genre>', views.genre, name='genre'),
    path("<genre>/<subgenre>", views.subgenre, name='subgenre'),
    path("<genre>/<subgenre>/<game>", views.game, name='game'),
    
]