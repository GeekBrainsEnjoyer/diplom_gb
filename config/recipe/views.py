from django.shortcuts import get_object_or_404, render

from .models import Recipe


def detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe/detail.html', {
        'recipe': recipe})
