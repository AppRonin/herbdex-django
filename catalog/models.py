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
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="herbs")
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
    
class MedicalUse(models.Model):
    name = models.CharField(max_length=50)
    observation = models.TextField(blank=True)
    herb = models.ForeignKey(Herb, on_delete=models.CASCADE, related_name="medical_uses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # avoids duplications in same herb
        unique_together = ("name", "herb")

    def __str__(self):
        return "f{self.name} ({self.herb.NAME})"
    
    