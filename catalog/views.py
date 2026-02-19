from django.shortcuts import render, get_object_or_404
from .models import Herb

# Create your views here.
def catalog(request):
    herbs = Herb.objects.all()

    context = {'herbs': herbs}

    return render(request, 'catalog/catalog.html', context)

def herb_detail(request, herb_slug):
    herb = get_object_or_404(Herb, slug=herb_slug)

    context = {'herb': herb}

    return render(request, 'catalog/herb_detail.html', context)

def about(request):
    return render(request, 'catalog/about.html')