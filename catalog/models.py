from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Herb(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    scientific_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="herbs")
    overview = models.TextField(blank=True)
    catalog_image = models.ImageField(upload_to='images/herbs/catalog', blank=True, null=True)
    detail_image = models.ImageField(upload_to='images/herbs/detail', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('herb_detail', args=[self.slug])

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name