from django.db import models
from django.urls import reverse
from datetime import datetime


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Recipe(models.Model):
    DIFFICULTY_CHOICES = (
        ("EASY", "easy"),
        ("MEDIUM", "medium"),
        ("HARD", "hard")
    )
    recipe_header = models.CharField(max_length=255)
    ingredients_header = models.CharField(max_length=50, default="Ingredients:")
    ingredients = models.TextField(default="")
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    difficulty_level = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default="EASY")
    preparation_time = models.CharField(max_length=10, default="0 min")
    date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='recipes_images', blank=True, null=True)

    def __str__(self):
        return self.recipe_header

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={"pk": self.pk})

    def get_ingredients(self):
        if self.ingredients:
            return [i.strip() for i in self.ingredients.split(",")]
        return ""

    class Meta:
        ordering = ['-date']
