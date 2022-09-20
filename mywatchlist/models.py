from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched_film = models.CharField(max_length=255)
    title_film = models.TextField()
    rating_film = models.TextField()
    release_date = models.TextField()
    review_film = models.TextField()