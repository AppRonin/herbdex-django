from django.contrib import admin
from .models import Herb, Category, MedicalUse

# Register your models here.
class HerbAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'created_at', 'updated_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

class MedicalUseAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_herbs', 'created_at', 'updated_at')

    def get_herbs(self, obj):
        return ", ".join([h.name for h in obj.herbs.all()])

    get_herbs.short_description = "Herbs"

admin.site.register(Herb, HerbAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MedicalUse, MedicalUseAdmin)