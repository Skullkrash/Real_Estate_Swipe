from django.db import models
from time import timezone

# Create your models here.

class Message(models.Model):
    content = models.CharField(max_length=100,null=False)
    date = models.DateField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.name


class Conversation(models.Model):

    def __str__(self):
        return self.name


class User(models.Model):
    firstName = models.CharField(max_length=100,null=False)
    lastName = models.CharField(max_length=100,null=False)
    email = models.CharField(max_length=100,null=False)
    password = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name


class Property(models.Model):
    label = models.CharField(max_length=500,null=False)
    type = models.CharField(max_length=1,null=False)
    description = models.CharField(max_length=500,null=False)
    surface = models.IntegerField(null=False)
    nbrRoom = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    isRental = models.BooleanField(default=True)

    def __str__(self):
        return self.name
        

class Advantage(models.Model):
    label = models.CharField(max_length=500,null=False)
    icon = models.CharField(max_length=500,null=False) # Not sure about this one, ask Alexis what it should be

    def __str__(self):
        return self.name



# Examples : 
'''
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Drink(models.Model):
    type = models.ForeignKey(Category, on_delete=models.CASCADE) 
    name = models.CharField(max_length=50)
    prize = models.IntegerField()

    SIZES = [ #Field choices
        ("S", "Small"), # ("BDD value", "Display name")
        ("M", "Medium"),
        ("L", "Large"), 
        ("F", "Fat")
    ]
    size = models.CharField(max_length=1, choices=SIZES)
    
    
    def __str__(self):
        return self.name + " " + str(self.type)
'''