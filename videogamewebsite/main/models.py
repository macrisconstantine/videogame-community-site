from django.db import models
from django.contrib.auth import get_user_model

class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField("Genre slug", null=True, blank=True, unique=True)

    def __str__(self):
        return self.name
    
class SubGenre(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)

    subgenre_slug = models.SlugField("Subgenre slug", null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

class VideoGame(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    game_slug = models.SlugField("Game slug", null=True, blank=True, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    sub_genre = models.ForeignKey(SubGenre, on_delete=models.CASCADE)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
