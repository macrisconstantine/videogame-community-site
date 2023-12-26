from django.urls import path
from . import views

# Urls to handle view functionality for the main app
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('search/', views.search, name='search'),
    path('<genre>', views.genre, name='genre'),
    path("<genre>/<subgenre>", views.subgenre, name='subgenre'),
    path("<genre>/<subgenre>/<game>", views.game, name='game'),
    path('rate_game/<int:game_id>/<int:rating>/', views.rate_game, name='rate_game'),

]