from django.contrib import admin
from .models import Genre, VideoGame

# Register your models here.
admin.site.register(Genre)
admin.site.register(VideoGame)