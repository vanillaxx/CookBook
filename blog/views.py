from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Recipe, Tag


def home(request):
    recipes = Recipe.objects.filter(status='PUB').order_by('published_at')
    return render(request, 'blog/home.html', {'recipes': recipes})


def tags_list(request):
    tags = Tag.objects.all().order_by('name')
    return render(request, 'blog/tags_list.html', {'tags': tags})