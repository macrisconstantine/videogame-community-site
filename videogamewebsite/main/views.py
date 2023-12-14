from django.shortcuts import render, get_object_or_404
from .models import Genre, VideoGame, SubGenre
from django.db.models.query_utils import Q

from django.http import JsonResponse

def rate_game(request, game_id, rating):
    # Assuming you have a VideoGame model with a ForeignKey to User
    user = request.user
    game = VideoGame.objects.get(id=game_id)

    # Update the game's rating
    game.total_ratings += 1
    game.average_rating = ((game.average_rating * (game.total_ratings - 1)) + int(rating)) / game.total_ratings
    game.save()

    # You might want to store the user's rating in a separate model if you want to prevent multiple ratings by the same user.

    return JsonResponse({'message': 'Rating submitted successfully'})

def search(request):
    search_query = request.GET.get('search_query', '')
    
    # Perform the search logic based on your model
    objects = VideoGame.objects.filter(
        Q(title__icontains=search_query)|Q(platform__icontains=search_query)
    )
    print(objects)
    return render(
        request=request,
        template_name='main/home.html',  # Create this template
        context={'objects': objects, 'search_query': search_query}
    )
    
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
    # I almost died over this line of code
    matching_subgenre = VideoGame.objects.filter(subgenre__genre__slug=genre, subgenre__subgenre_slug=subgenre).all()
    
    return render(
        request=request,
        template_name='main/home.html',
        context={"objects": matching_subgenre}
        )


def game(request, genre: str, subgenre: str, game: str):
    matching_game = VideoGame.objects.filter(subgenre__genre__slug=genre, game_slug=game).first()
    
    return render(
        request=request,
        template_name='main/game.html',
        context={"object": matching_game}
    )
