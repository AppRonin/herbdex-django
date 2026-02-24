from modeltranslation.translator import register, TranslationOptions
from .models import Herb, Category, MedicalUse, Observation


@register(Herb)
class HerbTranslationOptions(TranslationOptions):
    fields = ('name', 'overview')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(MedicalUse)
class MedicalUseTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Observation)
class ObservationTranslationOptions(TranslationOptions):
    fields = ('content',)