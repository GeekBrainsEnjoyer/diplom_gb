from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Recipe


from .forms import RecipeForm


def detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe/detail.html', {
        'recipe': recipe})


@login_required
def new_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            recipe = form.save(False)
            recipe.created_by = request.user
            recipe.save()

            return redirect('recipe:detail', pk=recipe.id)

    else:
        form = RecipeForm()

    return render(request, 'recipe/recipe_form.html', {'form': form, 'title': 'Новый рецепт'})


@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)

        if form.is_valid():
            recipe.save()

            return redirect('recipe:detail', pk=recipe.id)

    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipe/recipe_form.html', {'form': form, 'title': 'Изменить рецепт'})


@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, created_by=request.user)
    recipe.delete()

    return redirect('core:index')
