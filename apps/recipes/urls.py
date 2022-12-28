from django.urls import path
# from recipes.views import recipe_crud, searcher
from apps.recipes.views import recipe_crud, searcher


urlpatterns = [
    path('', recipe_crud.index, name='index'),
    path('<int:recipe_id>', recipe_crud.recipe, name='recipe'),
    path('search', searcher.search, name='search'),
    path('create/recipe', recipe_crud.create_recipe, name='create_recipe'),
    path('delete/recipe/<int:recipe_id>', recipe_crud.delete_recipe, name='delete_recipe'),
    path('edit/recipe/<int:recipe_id>', recipe_crud.edit_recipe, name='edit_recipe'),
    path('update_recipe', recipe_crud.update_recipe, name='update_recipe')
]
