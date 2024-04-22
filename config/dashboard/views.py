from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from recipe.models import Recipe


@login_required
def index(request):
    recipe_set = Recipe.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {'recipe_set': recipe_set})
