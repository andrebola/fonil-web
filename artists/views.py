from django.shortcuts import render, get_object_or_404
import models

def main(request):
    artists = models.Artist.objects.order_by('?')[:20]

    ret = {
            "artists": artists,
            }
    return render(request, "artists/index.html", ret)

def genres(request):
    genres = models.Genre.objects
    artists = models.Artist.objects
    ret = {
            "artists": artists,
            "genres": genres,
            "all_genres": True
          }
    return render(request, "artists/genres.html", ret)

def genre(request, genre_id):
    genres = models.Genre.objects
    genre = get_object_or_404(models.Genre, pk=genre_id)

    artists = models.Artist.objects.filter(genres__in=[genre])
    ret = {
            "artists": artists,
            "genres": genres,
            "genre": genre
          }
    return render(request, "artists/genres.html", ret)

def search(request):
    query = request.GET.get("q", None)
    artists = models.Artist.objects.filter(name__icontains=query)

    ret = {
            "artists": artists,
            "query": query,
            }
    return render(request, "artists/search.html", ret)

def artist(request, uuid):
    artist = get_object_or_404(models.Artist, uuid=uuid)
    ret = {"artist": artist}
    return render(request, "artists/artist.html", ret)
