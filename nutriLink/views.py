from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from nutriLink.models import Recipe, Diet, User


# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)
def index(request):
    recipe_list = Recipe.objects.order_by('-pub_date')
    # recipe_list = Diet.objects.filter()
    templete = loader.get_template('nutriLink/index.html')
    # output = ", ".join([q.diet_name for q in recipe_list])
    context = {'recipe_list': recipe_list, }
    return HttpResponse(templete.render(context, request))

def recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404('Recipe does not exist')
    return render(request, "nutriLink/recipe.html", {'recipe': recipe})

def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, "nutriLink/user.html", {'user': user})

def recipe_form(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404('User does not exist') # NIEZSLOGOWANY UŻYTKOWNIK
    return render(request, "nutriLink/recipe_form.html", {'user': user})

def user_form(request):
    message = "Sign up"
    context = {'message': message}
    return render(request, "nutriLink/user_form.html", context)