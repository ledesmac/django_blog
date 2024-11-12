from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Author (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=350)
    img_name  = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(default="", blank= True, null=False, db_index=True) 
    content = models.CharField(max_length=10000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    

    