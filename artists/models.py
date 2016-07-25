import uuid
from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=254)

    class Meta:
        ordering = ["name"]

class Artist(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=254)
    fbid = models.CharField(max_length=254)
    description = models.TextField(max_length=3000, blank=True, null=True)
    location = models.CharField(max_length=254, blank=True, null=True)
    hometown = models.CharField(max_length=254, blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)
    website = models.CharField(max_length=254, blank=True, null=True)
    fb_link = models.CharField(max_length=254, blank=True, null=True)
    twitter_link = models.CharField(max_length=254, blank=True, null=True)
    soundcloud_link = models.CharField(max_length=254, blank=True, null=True)
    bandcamp_link = models.CharField(max_length=254, blank=True, null=True)
    spotify_link = models.CharField(max_length=254, blank=True, null=True)
    youtube_link = models.CharField(max_length=254, blank=True, null=True)
    image = models.CharField(max_length=254, blank=True, null=True)
    genres = models.ManyToManyField(Genre)
    similar = models.ManyToManyField('Artist')
    date = models.DateTimeField(auto_now=True)

LINK_CHOICES = (
        ('yt', 'Youtube'),
        ('sf', 'Spotify'),
        ('sc', 'Soundcloud'),
)

class Link(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    url = models.CharField(max_length=254)
    link_type = models.CharField(max_length=2, choices=LINK_CHOICES)
    name = models.CharField(max_length=254, blank=True, null=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True)
    comment = models.TextField(max_length=3000)

    submit_date = models.DateTimeField(default=None, db_index=True)

class Post(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    url = models.CharField(max_length=254)
    text = models.TextField(max_length=3000, blank=True, null=True)
    date = models.DateTimeField()


