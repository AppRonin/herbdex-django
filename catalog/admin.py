import catalog.translation

from django.contrib import admin
from .models import Herb, Category, MedicalUse, Observation

from modeltranslation.admin import TranslationAdmin

# Register your models here.
@admin.register(Herb)
class HerbAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'created_at', 'updated_at')

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(MedicalUse)
class MedicalUseAdmin(TranslationAdmin):
    list_display = ('name', 'herb', 'created_at', 'updated_at')

@admin.register(Observation)
class ObservationAdmin(TranslationAdmin):
    list_display = ("medical_use", "content")
    search_fields = ("content", "medical_use__name", "medical_use__herb__name")