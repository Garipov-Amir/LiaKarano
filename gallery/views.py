from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from gallery.models import Picture

def Home(request):
    allpictures = Picture.objects.all()
    return render(request, 'Home.html',{'pictures':allpictures})

def picture(request, pic_id):
    picture = Picture.objects.get(pk=pic_id)
    if picture != None:
        return render(request, 'Picture.html', {'picture': picture})
    else:
        raise Http404("Sorry, but this picture doesn't exist")