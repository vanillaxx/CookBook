from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DetailView, DeleteView
from .models import Recipe, Tag


# Create your views here.
def home(request):
    recipes = Recipe.objects.all()
    tags = Tag.objects.all()
    return render(request,
                  'blog/home.html',
                  {'recipes': recipes,
                   'tags': tags})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', {'tags': tags})


def tag(request, pk):
    recipes = Recipe.objects.filter(tags__pk=pk)
    tags = Tag.objects.all()
    return render(request,
                  'blog/home.html',
                  {'recipes': recipes,
                   'tags': tags})


def difficulty_lvl(request, level):
    recipes = Recipe.objects.filter(difficulty_level=level)
    tags = Tag.objects.all()
    return render(request,
                  'blog/home.html',
                  {'recipes': recipes,
                   'tags': tags})


class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['recipe_header', 'ingredients', 'description', 'tags',
              'difficulty_level', 'preparation_time', 'image']
    template_name = "blog/recipe_update.html"


class RecipeCreate(CreateView):
    model = Recipe
    fields = ['recipe_header', 'ingredients', 'description', 'tags',
              'difficulty_level', 'preparation_time', 'image']
    template_name = "blog/recipe_create.html"


class RecipeDelete(DeleteView):
    model = Recipe
    fields = ['recipe_header', 'ingredients', 'description', 'tags',
              'difficulty_level', 'preparation_time', 'image']
    template_name = "blog/recipe_delete.html"
    success_url = reverse_lazy('home')


class TagCreate(CreateView):
    model = Tag
    fields = ['name']
    template_name = "blog/tag_create.html"
    success_url = '/tags'


class TagDelete(DeleteView):
    model = Tag
    fields = ['name']
    template_name = "blog/tag_delete.html"
    success_url = '/tags'


class RecipeDisplay(DetailView):
    model = Recipe
