from django.db import models
from django.conf import settings
from django.utils import timezone

class Pokemon(models.Model):
    """
    The Pokemon model is the characteristics of the Pokemon that the Pokedex will output to the user.
    This model is not being currently used, but was prepared for the second iteration of this project!
    
    """

    name = models.CharField(max_length=50)
    gameIndex = models.CharField(max_length=4)
    genus = models.CharField(max_length=50)
    appearanceURL = models.CharField(max_length=200)
    flavortext = models.TextField()
    types = models.CharField(max_length=100)

    def __str__(self):
        return self.name;