from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify
import os
import users
from users.models import CustomUser

# Model representing Video Game Genres
class Genre(models.Model):
    # Function to generate the upload path for images
    def image_upload_to(self, instance=None, filename=None):
        if instance:
            return os.path.join("Genre", slugify(self.slug), filename)
        return None
    
    title = models.CharField(max_length=100)
    slug = models.SlugField("Genre slug", null=True, blank=True, unique=True)
    image = models.ImageField(null=False, blank=False, upload_to=image_upload_to, max_length=255)
    class_name = " Genres"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Genres"
        ordering = ['title']

class SubGenre(models.Model):
    def image_upload_to(self, instance=None, filename=None):
        if instance:
            return os.path.join('Subgenre', slugify(self.genre.slug), slugify(self.subgenre_slug), filename)
        return None

    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    subgenre_slug = models.SlugField("Subgenre slug", null=True, blank=True, unique=True)
    image = models.ImageField(null=False, blank=False, upload_to=image_upload_to, max_length=255)
    class_name = " Subgenres"

    def __str__(self):
        return self.title
    
    # Property to get a concatenated slug
    @property
    def slug(self):
        return os.path.join(self.genre.slug, self.subgenre_slug)

    class Meta:
        verbose_name_plural = "Subgenres"
        ordering = ['title']

# Model representing Video Games
class VideoGame(models.Model):
    def image_upload_to(self, instance=None, filename=None):
        if instance:
            return os.path.join('VideoGame', slugify(self.genre.slug), slugify(self.subgenre.subgenre_slug), slugify(self.game_slug), filename)
        return None

    # Attributes of the video game model
    title = models.CharField(max_length=200)
    platform = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    release_date = models.DateField()
    game_slug = models.SlugField("Game slug", null=False, blank=False, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    subgenre = models.ForeignKey(SubGenre, on_delete=models.CASCADE)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='created_games')
    image = models.ImageField(upload_to=image_upload_to, max_length=255, null=False, blank=False)
    average_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    total_ratings = models.PositiveIntegerField(default=0)
    
    # Many-to-Many relationship with a through model 'UserClick'
    clicks = models.ManyToManyField(get_user_model(), through='UserClick', related_name='clicked_games')
    class_name = "s"
    
    def __str__(self):
        return self.title
    
    # Property to get a concatenated slug
    @property
    def slug(self):
        return os.path.join(self.subgenre.slug, self.game_slug)

    class Meta:
        verbose_name_plural = "Video games"
        ordering = ['-release_date']

# Model representing User Clicks on Video Games
class UserClick(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    game = models.ForeignKey(VideoGame, on_delete=models.CASCADE)
    click_timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username + " clicked " + self.game.title
