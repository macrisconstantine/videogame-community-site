from django.shortcuts import render, get_object_or_404
from .models import Genre, UserClick, VideoGame, SubGenre
from django.db.models.query_utils import Q

from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count


# Authorizes user before allowing them to rate a game
@user_passes_test(lambda u: u.is_authenticated, login_url='/login')
def rate_game(request, game_id, rating):
    # user = request.user # for future implementation of limiting ratings to one per user per game
    game = VideoGame.objects.get(id=game_id)

    # Update the game's rating
    game.total_ratings += 1
    game.average_rating = ((game.average_rating * (game.total_ratings - 1)) + int(rating)) / game.total_ratings
    game.save()

    # In the future I will liekely store the user's rating in a separate model to prevent multiple ratings by the same user.

    return JsonResponse({'message': 'Rating submitted successfully'})

# View to handle search functionality
def search(request):
    search_query = request.GET.get('search_query', '')
    
    # Checks if either the game title or game platform contains the search query
    objects = VideoGame.objects.filter(
        Q(title__icontains=search_query)|Q(platform__icontains=search_query)
    )
    
    # Renders the homepage along with the search results
    return render(
        request=request,
        template_name='main/home.html',  # Create this template
        context={'objects': objects, 'search_query': search_query}
    )
    
# View to handle the homepage: when homepage is requested, this view is called
# and returns one of two templates depending on whether the user is authenticated.
def homepage(request):
    matching_genre = Genre.objects.all()
    if request.user.is_authenticated:
        
        # Assuming you have a user object or user ID
        user_id = request.user.id

        # Get the most clicked platform for the user
        most_clicked_platform = UserClick.objects.filter(user_id=user_id).values('game__platform').annotate(click_count=Count('game__platform')).order_by('-click_count').first()
        print(most_clicked_platform)
        
        # Get games in the most clicked platform
        if most_clicked_platform:
            recommended_games = VideoGame.objects.filter(platform=most_clicked_platform['game__platform'])[:5]
            print(recommended_games)
        else:
            
            # If there's no click history, just recommend some popular games
            recommended_games = VideoGame.objects.all()[:5]
    
        return render(
            request=request,
            template_name='main/home.html',
            context={"objects": matching_genre, "recommended_games": recommended_games}
            )
    else:
        return render(
            request=request,
            template_name='main/home.html',
            context={"objects": matching_genre}
            )

# I ran out of time to properly modularize this code, so I just copied and pasted it
# from the homepage view and made a few changes to get it to work.
def genre(request, genre: str):
    matching_genre = SubGenre.objects.filter(genre__slug=genre).all()
    if request.user.is_authenticated:
        # Assuming you have a user object or user ID
        user_id = request.user.id

        # Get the most clicked platform for the user
        most_clicked_platform = UserClick.objects.filter(user_id=user_id).values('game__platform').annotate(click_count=Count('game__platform')).order_by('-click_count').first()
        print(most_clicked_platform)
        # Get games in the most clicked platform
        if most_clicked_platform:
            recommended_games = VideoGame.objects.filter(platform=most_clicked_platform['game__platform'])[:5]
            print(recommended_games)
        else:
            # If there's no click history, just recommend some popular games
            recommended_games = VideoGame.objects.all()[:5]
    
        return render(
            request=request,
            template_name='main/home.html',
            context={"objects": matching_genre, "recommended_games": recommended_games}
            )
    else:
        return render(
            request=request,
            template_name='main/home.html',
            context={"objects": matching_genre}
            )

# Same as above, but for subgenres filtered by genre
def subgenre(request, genre: str, subgenre: str):
    # I almost died over this line of code
    matching_subgenre = VideoGame.objects.filter(subgenre__genre__slug=genre, subgenre__subgenre_slug=subgenre).all()
    if request.user.is_authenticated:
        # Assuming you have a user object or user ID
        user_id = request.user.id

        # Get the most clicked platform for the user
        most_clicked_platform = UserClick.objects.filter(user_id=user_id).values('game__platform').annotate(click_count=Count('game__platform')).order_by('-click_count').first()
        print(most_clicked_platform)
        # Get games in the most clicked platform
        if most_clicked_platform:
            recommended_games = VideoGame.objects.filter(platform=most_clicked_platform['game__platform'])[:5]
            print(recommended_games)
        else:
            # If there's no click history, just recommend some popular games
            recommended_games = VideoGame.objects.all()[:5]
    
        return render(
            request=request,
            template_name='main/home.html',
            context={"objects": matching_subgenre, "recommended_games": recommended_games}
            )
    else:
        return render(
            request=request,
            template_name='main/home.html',
            context={"objects": matching_subgenre}
            )

# Renders the game page with the games specified by the url
def game(request, genre: str, subgenre: str, game: str):
    matching_game = VideoGame.objects.filter(subgenre__genre__slug=genre, game_slug=game).first()
    
    # Assuming the user is authenticated
    if request.user.is_authenticated:
        # Record the user click
        UserClick.objects.create(user=request.user, game=matching_game)

    
    return render(
        request=request,
        template_name='main/game.html',
        context={"object": matching_game}
    )
