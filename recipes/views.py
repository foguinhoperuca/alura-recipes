from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe


def index(request):
    # return HttpResponse('<h1>Recipes - By Alura</h1><h2>Welcome, Padwan!!</h2>')

    context = {
        'name_recipes': {
            1: 'Lasagna',
            2: 'Vegetables Soup',
            3: 'Ice Cream',
            4: 'Choco Cake'
        }
    }
    # context = {
    #     'recipes': Recipe.objects.all()
    # }

    return render(request, 'index.html', context)

def recipe(request):
    return render(request, 'recipe.html')
