from django.contrib import admin
from .models import Recipe


# Register your models here.
class ListingRecipe(admin.ModelAdmin):
    list_display = ('id', 'name', 'preparation_time', 'date_recipe', 'publicated', 'person')
    list_display_links = ('id', 'name')
    search_fields = ['name']
    list_filter = ['category']
    list_per_page = 2
    list_editable = ('publicated',)
    ordering = ['name']


admin.site.register(Recipe, ListingRecipe)
