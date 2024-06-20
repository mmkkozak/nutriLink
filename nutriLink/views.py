from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from nutriLink.forms import SignupForm, LoginForm, NewRecipeForm
from nutriLink.models import Recipe, Diet, User

"""
def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, "nutriLink/user.html", {'user': user, 'user_id': user_id})


def user_form(request):
    message = "Sign up"
    context = {'message': message}
    return render(request, "nutriLink/user_form.html", context)


def results(request, recipe_id):
    response = "Some response %s."
    return HttpResponse(response % recipe_id)


def get_new_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    else:
        form = SignUpForm()

    return render(request, "nutriLink/sign_up.html", {"form": form})


def insertUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if request.POST['user_password'] == request.POST['password_confirm']:
                user_name = request.POST['user_name']
                user_email = request.POST['user_email']
                user_password = request.POST['user_password']
                NewUser = User(name=user_name, email=user_email, password=user_password)
                NewUser.save()
                return render(request, "nutriLink/sign_up.html", {"message": "User added successfully", "form": form})
            else:
                return render(request, "nutriLink/sign_up.html", {"message": "Passwords don't match", "form": form})
        else:
            return HttpResponse("Insert data!")


def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
    else:
        form = LoginForm()

    return render(request, "nutriLink/sign_in.html", {"form": form})


def verify_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = request.POST['user_name']
            try:
                q = User.objects.get(name=name)
                if q.password == request.POST['user_password']:
                    request.session["user_id"] = q.id
                    return render(request, "nutriLink/redirect.html", {"value": q.id})
                else:
                    return HttpResponse("Username or password are incorrect")
            except:
                return render(request, "nutriLink/sign_in.html", {"form": form, "message": "Username or password is incorrect"})


def insert_recipe(request, user_id):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe_name = request.POST['recipe_name']
            contents = request.POST['contents']
            picture = request.POST['picture']
            pub_date = request.POST['pub_date']
            # new_recipe = Recipe(recipe_name=recipe_name, contents=contents, picture=picture, pub_date=pub_date, user_id=request.session["user_id"])
            new_recipe = Recipe(recipe_name=recipe_name, contents=contents, picture=picture, pub_date=pub_date, user_id=user_id)
            new_recipe.save()
            return render(request, 'nutriLink/recipe_form.html', {"form": form, "message": "New recipe added successfully",'user_id': request.session["user_id"]})
        else:
            return render(request, 'nutriLink/recipe_form.html', {"form": form, "message": "Insert valid recipe details",'user_id': request.session["user_id"]})


def logout(request):
    if request.session["user_id"] != "":
        del request.session['user_id']
        
"""

def index(request):
    recipes = Recipe.objects.all()
    diets = Diet.objects.all()
    return render(request, 'nutriLink/index.html',{
        'recipes': recipes,
        'diets': diets
    })

# def contact(request):
#     return render(request, 'nutriLink/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'nutriLink/signup.html',{
        'form': form
    })

def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    try:
        return render(request, 'nutriLink/recipe.html', {
            'recipe': recipe,
        })
    except (KeyError, Recipe.DoesNotExist):
        return render(
            request,
            "nutriLink/recipe.html",
            {
                'recipe': recipe,
                'error_message': "Przepis nie istnieje.",
            },
        )

@login_required
def new_recipe(request):
    if request.method == 'POST':
        form = NewRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()

            return redirect('nutriLink:recipe', pk=recipe.id)
    else:
        form = NewRecipeForm()

    return render(request, 'nutriLink/recipe_form.html', {
        'form': form,
        'title': 'Dodaj przepis',
    })

@login_required
def profile(request):
    recipes = Recipe.objects.filter(user=request.user)

    return render(request, 'nutriLink/user.html', {
        'recipes': recipes,
    })

def recipe_text(request, pk):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=Recipe.txt'
    q = Recipe.objects.get(id=pk)
    ingredients = q.contents
    response.writelines(ingredients)
    return response