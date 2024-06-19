from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from nutriLink.forms import SignupForm, LoginForm, NewRecipeForm
from nutriLink.models import Recipe, Diet, Review


def index(request):
    recipes = Recipe.objects.all()
    diets = Diet.objects.all()
    
    if request.method == 'POST':
        logout(request)
        del request.session['user_id']
        return redirect('nutriLink/')

    return render(request, 'nutriLink/index.html',{
        'recipes': recipes,
        'diets': diets
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('nutriLink/login/')

    else:
        form = SignupForm()

    return render(request, 'nutriLink/signup.html',{
        'form': form
    })

def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    reviews = Review.objects.filter(recipe=recipe)
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
                'reviews': reviews,
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