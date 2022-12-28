from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from termcolor import colored
# from recipes.models import Recipe
from apps.recipes.models import Recipe


def index(request):
    paginator = Paginator(Recipe.objects.filter(publicated=True).order_by('-date_recipe'), 3)
    recipes_per_page = paginator.get_page(request.GET.get('page'))

    context = {
        'recipes': recipes_per_page
    }

    return render(request, 'recipes/index.html', context)


def recipe(request, recipe_id):
    r = get_object_or_404(Recipe, pk=recipe_id)

    context = {
        'recipe': r
    }

    return render(request, 'recipes/recipe.html', context)


def create_recipe(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = get_object_or_404(User, pk=request.user.id)
            print(colored(f'Create Recipe!! {request.POST["name_recipe"] = } {request.POST["ingredients"] = } '
                          f'{request.POST["preparation"] = } {request.POST["preparation_time"] = } '
                          f'{request.POST["serving"] = } {request.POST["category"] = } {request.FILES["photo"] = }'
                          f'{user = }',
                          'green', attrs=['bold']))

            r = Recipe.objects.create(person=user, name=request.POST["name_recipe"],
                                      ingredients=request.POST["ingredients"],
                                      preparation=request.POST["preparation"],
                                      preparation_time=request.POST["preparation_time"],
                                      serving=request.POST["serving"], category=request.POST["category"],
                                      photo=request.FILES["photo"])
            r.save()

            return redirect('/recipe_users/dashboard')

        return render(request, 'recipes/create_recipe.html')
    else:
        return redirect('recipes/index')


def delete_recipe(request, recipe_id):
    r = get_object_or_404(Recipe, pk=recipe_id)
    r.delete()
    print(colored(f"Recipe #{recipe_id} successfully deleted!!", "green", attrs=["bold"]))
    messages.success(request, f"Recipe #{recipe_id} successfully deleted!!")

    return redirect('/recipe_users/dashboard')


def edit_recipe(request, recipe_id):
    r = get_object_or_404(Recipe, pk=recipe_id)
    context = {
        'recipe': r
    }
    print(colored(f"Recipe #{recipe_id} successfully loaded!!", "green", attrs=["bold"]))
    messages.success(request, f"Recipe #{recipe_id} successfully loaded!!")

    return render(request, 'recipes/edit_recipe.html', context)


def update_recipe(request):
    if request.method == 'POST':
        recipe_id = request.POST['recipe_id']
        r = Recipe.objects.get(pk=recipe_id)
        r.name = request.POST['name']
        r.ingredients = request.POST['ingredients']
        r.preparation = request.POST['preparation']
        r.preparation_time = request.POST['preparation_time']
        r.serving = request.POST['serving']
        r.category = request.POST['category']
        if 'photo' in request.FILES:
            r.photo = request.FILES['photo']

        r.save()

        print(colored(f"Recipe #{recipe_id} successfully updated!!", "green", attrs=["bold"]))
        messages.success(request, f"Recipe #{recipe_id} successfully updated!!")

        return redirect('/recipe_users/dashboard')
