from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from comments.forms import CommentForm
from comments.models import Comment
from .models import Recipe, Category
from django.db.models import Q


from .forms import RecipeForm


def detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    comments = Comment.objects.filter(recipe=recipe).order_by("-pk")

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)

        if comment_form.is_valid():
            comment = comment_form.save(False)
            comment.recipe = recipe
            comment.created_by = request.user
            comment.save()

            return redirect('recipe:detail', pk=recipe.id)

    else:
        comment_form = CommentForm()

    return render(request, 'recipe/detail.html', {
        'recipe': recipe,
        'comment_form': comment_form,
        'comments': comments})


def browse(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    recipe_set = Recipe.objects.all()
    category_set = Category.objects.all()

    if category_id:
        recipe_set = recipe_set.filter(category_id=category_id)

    if query:
        recipe_set = recipe_set.filter(Q(name__icontains=query) | Q(
            description__icontains=query) | Q(steps__icontains=query))

    return render(request, 'recipe/browse.html', {
        'category_set': category_set, 'recipe_set': recipe_set, 'category_id': int(category_id)})


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
