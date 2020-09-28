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
