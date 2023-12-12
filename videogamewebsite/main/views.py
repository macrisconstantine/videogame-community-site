from django.shortcuts import render, get_object_or_404
from .models import Genre, VideoGame, SubGenre

# Create your views here.
# def homepage(request):
#     return render(request, "main/home.html")

def games_by_genre(request, genre_slug):
    genre = get_object_or_404(Genre, slug=genre_slug)
    games = VideoGame.objects.filter(genre=genre)
    genres = Genre.objects.all()  # You may want to pass this for navigation
    return render(request, 'games_by_genre.html', {'genre': genre, 'games': games, 'genres': genres})

def games_by_subgenre(request, genre_slug, subgenre_slug):
    genre = get_object_or_404(Genre, slug=genre_slug)
    subgenre = get_object_or_404(SubGenre, slug=subgenre_slug)
    games = VideoGame.objects.filter(genre=genre, subgenre=subgenre)
    genres = Genre.objects.all()  # You may want to pass this for navigation
    return render(request, 'games_by_subgenre.html', {'genre': genre, 'subgenre': subgenre, 'games': games, 'genres': genres})

def homepage(request):
    matching_genre = Genre.objects.all()
    
    return render(
        request=request,
        template_name='main/home.html',
        context={"objects": matching_genre}
        )

def genre(request, genre: str):
    matching_genre = SubGenre.objects.filter(genre__slug=genre).all()
    
    return render(
        request=request,
        template_name='main/home.html',
        context={"objects": matching_genre}
        )
    
def subgenre(request, genre: str, subgenre: str):
    matching_subgenre = VideoGame.objects.filter(genre__slug=genre, subgenre_slug=subgenre).all()
    
    return render(
        request=request,
        template_name='main/home.html',
        context={"objects": matching_subgenre}
        )


def game(request, genre: str, subgenre: str, game: str):
    matching_game = VideoGame.objects.filter(genre__slug=genre, subgenre__slug=subgenre, game_slug=game).first()
    
    return render(
        request=request,
        template_name='main/game.html',
        context={"object": matching_game}
        )