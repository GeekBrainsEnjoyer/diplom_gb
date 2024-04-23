from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from recipe.models import Recipe


from .forms import SignupForm


def index(request):
    recipe_set = Recipe.objects.order_by('-created_at')[:5]

    return render(request, 'core/index.html',
                  {'recipe_set': recipe_set})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})
