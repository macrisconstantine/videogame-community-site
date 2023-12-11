from django.db import models
from django.contrib.auth import get_user_model

class Genre(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        if self.subcategory:
            return f"{self.name} - {self.subcategory}"
        return self.name

class VideoGame(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
