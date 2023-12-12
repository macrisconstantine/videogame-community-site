from django.contrib import admin
from .models import Genre, VideoGame, SubGenre


class VideoGameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'sub_genre', 'release_date', 'created_by')
    list_filter = ('genre', 'sub_genre', 'release_date', 'created_by')
    search_fields = ('title', 'genre', 'sub_genre', 'release_date', 'created_by')
    
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    
class SubGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    
# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(VideoGame, VideoGameAdmin)
admin.site.register(SubGenre, SubGenreAdmin)
