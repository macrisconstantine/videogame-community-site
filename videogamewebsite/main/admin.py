from django.contrib import admin
from .models import Genre, VideoGame, SubGenre, UserClick


class VideoGameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'subgenre', 'release_date', 'created_by', 'average_rating', 'platform',)
    list_filter = ('genre', 'subgenre', 'release_date', 'created_by', 'average_rating', 'platform',)
    search_fields = ('title', 'genre', 'subgenre', 'release_date', 'created_by', 'average_rating', 'platform',)
    
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    
class SubGenreAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    
class UserClickAdmin(admin.ModelAdmin):
    list_display = ('user','game',)
    list_filter = ('user','game',)
    search_fields = ('user','game',)
    
    
# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(VideoGame, VideoGameAdmin)
admin.site.register(SubGenre, SubGenreAdmin)
admin.site.register(UserClick, UserClickAdmin)

