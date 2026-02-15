from django.shortcuts import render
from .models import Herb

# Create your views here.
def catalog(request):
    herbs = Herb.objects.all()

    context = {'herbs': herbs}

    return render(request, 'catalog/catalog.html', context)