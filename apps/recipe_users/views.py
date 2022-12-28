from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from termcolor import colored
# from recipes.models import Recipe
from apps.recipes.models import Recipe


def register(request):
    """Register a new person in system"""
    if request.method == 'POST':
        print(f'User data: {request.POST["name"] = } {request.POST["email"] = }'
              f' {request.POST["password"] = } {request.POST["password2"] = }')

        if empty_field(request.POST["name"]):
            print(colored("Name can't be blank!!", 'yellow', attrs=['bold']))

            return redirect('register')

        if empty_field(request.POST["email"]):
            print(colored("E-mail can't be blank!!", 'yellow', attrs=['bold']))

            return redirect('register')

        if password_doesnt_match(request.POST["password"], request.POST["password2"]):
            print(colored("Passwords must match!!", 'yellow', attrs=['bold']))
            messages.error(request, "Passwords must match!!")

            return redirect('register')

        if User.objects.filter(email=request.POST["email"]).exists():
            print(colored("User EMAIL already registered!!", 'yellow', attrs=['bold']))
            messages.error(request, "User EMAIL already registered!!")

            return redirect('register')

        if User.objects.filter(username=request.POST["name"]).exists():
            print(colored("User USERNAME already registered!!", 'yellow', attrs=['bold']))
            messages.error(request, "User USERNAME already registered!!")

            return redirect('register')

        user = User.objects.create_user(username=request.POST["name"], email=request.POST["email"],
                                        password=request.POST["password"])
        user.save()
        print(colored("User successfully registered!!", 'blue', attrs=['bold']))
        messages.success(request, "User successfully registered!!")

        return redirect('login')

    return render(request, 'recipe_users/register.html')


def dashboard(request):
    """Show all recipes from a logged user"""
    if request.user.is_authenticated:
        recipes = Recipe.objects.order_by('-date_recipe').filter(person=request.user.id)

        context = {
            'recipes': recipes
        }

        return render(request, 'recipe_users/dashboard.html', context)
    else:
        return redirect('index')


def login(request):
    """Do login in site"""
    if request.method == 'POST':
        print(colored(f"{request.POST['email'] = } {request.POST['password'] = }", 'green', attrs=['bold']))
        if empty_field(request.POST["email"]) or empty_field(request.POST["password"]):
            print(colored("E-mail or password can't be blank!!", 'yellow', attrs=['bold']))
            messages.error(request, "E-mail or password can't be blank!!")

            return redirect('login')

        if User.objects.filter(email=request.POST["email"]).exists():
            name = User.objects.filter(email=request.POST["email"]).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=name, password=request.POST["password"])
            print(colored(f"{name = } {user = }", 'blue', attrs=['bold']))

            if user is not None:
                auth.login(request, user)
                print(colored(f'Login was done successfully!! {user.password = }', 'green', attrs=['bold']))
                messages.success(request, "Login was done successfully!!")
                return redirect('dashboard')

        return redirect('login')

    return render(request, 'recipe_users/login.html')


def logout(request):
    """Do logout in site"""
    auth.logout(request)
    messages.success(request, "Logout was done successfully!!")
    print(colored("Logout was done successfully!!", 'green', attrs=['bold']))

    return redirect('index')


def empty_field(field):
    """Helper to validate empty fields"""
    return not field.strip()


def password_doesnt_match(password, password2):
    """Helper to validate passwords"""
    return password != password2
