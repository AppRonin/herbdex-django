from django.contrib import admin
from .models import Herb, Category, MedicalUse, Observation

# Register your models here.
class HerbAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'created_at', 'updated_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

class MedicalUseAdmin(admin.ModelAdmin):
    list_display = ('name', 'herb', 'created_at', 'updated_at')

class ObservationAdmin(admin.ModelAdmin):
    list_display = ("medical_use", "content")
    search_fields = ("content", "medical_use__name", "medical_use__herb__name")


admin.site.register(Herb, HerbAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MedicalUse, MedicalUseAdmin)
admin.site.register(Observation, ObservationAdmin)