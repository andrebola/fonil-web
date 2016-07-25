from django.conf.urls import url
from artists import views

uuid_match = r'(?P<uuid>[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})'

urlpatterns = [
    url(r'^genres$', views.genres, name='artists-genres'),
    url(r'^genre/(?P<genre_id>\d+)$', views.genre, name='artists-genre'),
    url(r'^search$', views.search, name='artists-search'),
    url(r'^artist/%s$' % (uuid_match), views.artist, name='artists-artist'),
]
