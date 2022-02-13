from email.policy import default
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager 

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    tags = TaggableManager(blank=True)
    
    def get_absolute_url(self):
        return reverse("posts:view-post", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title 

    