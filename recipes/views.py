from django.shortcuts import render, get_object_or_404
from .models import Recipe


def index(request):
    context = {
        'recipes': Recipe.objects.filter(publicated=True).order_by('-date_recipe')
    }

    return render(request, 'index.html', context)


def recipe(request, recipe_id):
    r = get_object_or_404(Recipe, pk=recipe_id)

    context = {
        'recipe': r
    }

    return render(request, 'recipe.html', context)


def search(request):
    # return render(request, 'search_result.html')

    recipes = Recipe.objects.filter(publicated=True).order_by('-date_recipe')
    if 'search' in request.GET:
        query = request.GET['search']
        # TODO how to logging?!
        print(f"{query = }")
        if query:
            recipes = Recipe.objects.filter(name__icontains=f"{query}")

    context = {
        'recipes': recipes
    }

    return render(request, 'search_result.html', context)
