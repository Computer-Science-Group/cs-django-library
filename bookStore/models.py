from django.db import models


# Create your models here.

# Class for book tags
# eg: horror, fantasy ...etc
class Tag(models.Model):
    # The actual name of the tag
    tagName = models.CharField(max_length=30)
    # Description for the tag
    tagDescription = models.CharField(max_length=255)
    
    # Function that defines the row name in the database
    def __str__(self):
        return self.tagName


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)

    # a function to display the category like this example below
    # Adventure: this category is about journeys and fiction ...
    def __str__(self):
        return self.name + ': ' + self.description
