from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('create/recipe', views.create_recipe, name='create_recipe')
]
