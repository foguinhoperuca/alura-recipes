from django.shortcuts import render
from django.contrib import messages
from termcolor import colored
# from recipes.models import Recipe
from apps.recipes.models import Recipe


def search(request):
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

    print(colored(f"{len(recipes) = }"))
    messages.success(request, "Search result:")

    return render(request, 'recipes/search_result.html', context)
