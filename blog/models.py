from collectionfield.models import CollectionField
from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField, MonitorField


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Recipe(models.Model):
    DIFFICULTY_CHOICES = (
        ("EASY", "łatwe"),
        ("MEDIUM", "średnie"),
        ("HARD", "trudne")
    )
    recipe_header = models.CharField(max_length=255)
    ingredients_header = models.CharField(max_length=50, default="Składniki:")
    # ingredients = ArrayField(models.CharField(max_length=60))
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    difficulty_level = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default="EASY")
    STATUS = (
        ('DRAFT', "draft"),
        ('PUB', "published"))
    status = StatusField()
    published_at = MonitorField(monitor='status', when=['published'])

    def publish(self):
        self.status = 'PUB'
        self.save()

    def __str__(self):
        return self.recipe_header

    class Meta:
        ordering = ["-published_at"]
