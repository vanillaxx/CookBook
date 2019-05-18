from collectionfield.models import CollectionField
from django.db import models
from django.urls import reverse
from model_utils import Choices
from model_utils.fields import StatusField, MonitorField
import datetime

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    DIFFICULTY_CHOICES = (
        ("EASY", "łatwe"),
        ("MEDIUM", "średnie"),
        ("HARD", "trudne")
    )
    recipe_header = models.CharField(max_length=255)
    ingredients_header = models.CharField(max_length=50, default="Składniki:")
    ingredients = models.TextField(default="")
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    difficulty_level = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default="EASY")
    date = models.DateField(default=datetime.date.today)
    image = models.ImageField(upload_to='recipes_images',  blank=True, null=True)

    def __str__(self):
        return self.recipe_header

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-date"]
