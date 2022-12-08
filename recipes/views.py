from django.shortcuts import render, get_object_or_404
from .models import Recipe


def index(request):
    context = {
        'recipes': Recipe.objects.all()
    }

    return render(request, 'index.html', context)


def recipe(request, recipe_id):
    r = get_object_or_404(Recipe, pk=recipe_id)

    context = {
        'recipe': r
    }

    return render(request, 'recipe.html', context)
