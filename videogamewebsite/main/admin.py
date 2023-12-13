from django.contrib import admin
from .models import Genre, VideoGame, SubGenre


class VideoGameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'subgenre', 'release_date', 'created_by')
    list_filter = ('genre', 'subgenre', 'release_date', 'created_by')
    search_fields = ('title', 'genre', 'subgenre', 'release_date', 'created_by')
    
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    
class SubGenreAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    
# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(VideoGame, VideoGameAdmin)
admin.site.register(SubGenre, SubGenreAdmin)
