from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from gallery.models import Picture

def Home(request):
    allpictures = Picture.objects.all()
    return render(request, 'Home.html',{'pictures':allpictures})

