from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from nutriLink.forms import SignupForm, LoginForm, NewRecipeForm, ReviewForm
from nutriLink.models import Recipe, Diet, Review, Exclusion
from django.core.paginator import Paginator


def index(request):
    recipes = Recipe.objects.all()
    diets = Diet.objects.all()
    query = request.GET.get('dietlist', '')

    paginator = Paginator(recipes, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if query:
        recipes = recipes.filter()

    if request.method == 'POST':
        logout(request)
        del request.session['user_id']
        return redirect('nutriLink/')

    return render(request, 'nutriLink/index.html',{
        'recipes': recipes,
        'diets': diets,
        'query': query,
        'page_obj': page_obj,
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/nutriLink/login/')

    else:
        form = SignupForm()

    return render(request, 'nutriLink/signup.html',{
        'form': form
    })

def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    reviews = Review.objects.filter(recipe=recipe)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.recipe = recipe
            review.user = request.user
            review.save()
            return redirect('nutriLink:recipe', pk=pk)
    else:
        form = ReviewForm()

    try:
        return render(request, 'nutriLink/recipe.html', {
            'recipe': recipe,
            'reviews': reviews,
            'form': form,
        })
    except (KeyError, Recipe.DoesNotExist):
        return render(request,"nutriLink/recipe.html",{
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

def recipe_text(request, pk):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=Recipe.txt'
    q = Recipe.objects.get(id=pk)
    ingredients = q.contents
    response.writelines(ingredients)
    return response