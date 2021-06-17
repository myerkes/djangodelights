import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.
class Ingredient(models.Model):
    # Represents an Ingredient that can be used in multiple different recipes (MenuItems)
    POUNDS = 'lbs'
    CUPS = 'cups'
    TABLESPOONS = 'tbsp'
    TEASPOONS = 'tsp'
    EACH = 'each'
    UNIT_CHOICES = [
        (POUNDS, 'Pounds'),
        (CUPS, 'Cups'),
        (TABLESPOONS, 'Tablespoons'),
        (TEASPOONS, 'Teaspoons'),
        (EACH, 'Each')
    ]

    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=4, choices=UNIT_CHOICES)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return '/ingredients/'

class MenuItem(models.Model):
    # Represents an item on the restaurant menu
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.CharField(max_length=250); # Link to picture

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return '/menu/'

    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())

class RecipeRequirement(models.Model):
    # Represents a required amount of an ingredient for a recipe
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return str(self.quantity) + " - " + str(self.ingredient)

    def get_absolute_url(self):
        return '/reciperequirement/'

    def enough(self):
        return self.quantity <= self.ingredient.quantity


class Purchase(models.Model):
    # Represents a food order from the restaurant
    creation_date = models.DateTimeField(default=datetime.date.today)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return None

    def get_absolute_url(self):
        return '/menu/'

    def totalPrice(self):
        # For each Order in the Purchase, add the price of the order tot he total purchase price
        return self.menu_item

class Order(models.Model):
    # Represents an amount of MenuItems ordered in an order
    #price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField('MenuItem', related_name='order', blank=True)

    def __str__(self) -> str:
        return None
