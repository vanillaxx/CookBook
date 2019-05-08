from django.shortcuts import render
from django.shortcuts import redirect
import datetime

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DetailView, DeleteView

from .models import Recipe, Tag


def home(request):
    recipes = Recipe.objects.order_by('date')
    return render(request, 'blog/home.html', {'recipes': recipes})


def tags_list(request):
    tags = Tag.objects.all().order_by('name')
    return render(request, 'blog/tags_list.html', {'tags': tags})


class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['recipe_header', 'ingredients', 'description', 'tags', 'difficulty_level', 'image']
    template_name = "blog/recipe_update.html"


class RecipeCreate(CreateView):
    model = Recipe
    fields = ['recipe_header', 'ingredients', 'description', 'tags', 'difficulty_level', 'image']
    template_name = "blog/recipe_create.html"


class RecipeDelete(DeleteView):
    model = Recipe
    fields = ['recipe_header', 'ingredients', 'description', 'tags', 'difficulty_level', 'image']
    template_name = "blog/recipe_delete.html"
    success_url = reverse_lazy('home')


class TagCreate(CreateView):
    model = Tag
    fields = ['name']
    template_name = "blog/tag_create.html"
    success_url = '/tags'

    # def form_valid(self, form):
    #     self.object = form.save()
    #     return HttpResponseRedirect(self.get_success_url())
    #


class RecipeDisplay(DetailView):
    model = Recipe

