from django.shortcuts import render, get_object_or_404
from .models import Herb

from django.db.models import Q

# Create your views here.
def catalog(request):
    search_input = request.GET.get("search_input")

    herbs = Herb.objects.all()

    if search_input:
        herbs = herbs.filter(
            Q(name__icontains=search_input) |
            Q(medical_uses__name__icontains=search_input)
        ).distinct()

    context = {"herbs": herbs}
    
    return render(request, "catalog/catalog.html", context)

def herb_detail(request, herb_slug):
    herb = get_object_or_404(Herb, slug=herb_slug)

    context = {'herb': herb}

    return render(request, 'catalog/herb_detail.html', context)

def about(request):
    return render(request, 'catalog/about.html')