from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify
import os

class Genre(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.slug), instance)
        return None
    
    title = models.CharField(max_length=100)
    slug = models.SlugField("Genre slug", null=True, blank=True, unique=True)
    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255)



    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "Genres"
        ordering = ['title']
    
class SubGenre(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    subgenre_slug = models.SlugField("Subgenre slug", null=True, blank=True, unique=True)

    def __str__(self):
        return self.title
    
    @property
    def slug(self):
        return self.genre.slug + "/" + self.subgenre_slug

    class Meta:
        verbose_name_plural = "Subgenres"
        ordering = ['title']

class VideoGame(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('VideoGame', slugify(self.slug), instance)
        return None
        
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    game_slug = models.SlugField("Game slug", null=True, blank=True, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    subgenre = models.ForeignKey(SubGenre, on_delete=models.CASCADE)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image= models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to, max_length=255)
    

    def __str__(self):
        return self.title
    
    @property
    def slug(self):
        return self.subgenre.slug + "/" + self.game_slug

    class Meta:
        verbose_name_plural = "Video games"
        ordering = ['-release_date']