from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from nutriLink.forms import SignUpForm, LoginForm, RecipeForm
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
    if request.session['user_id'] != "":
        q = User.objects.get(id=request.session['user_id'])
        name = q.name
        context = {'recipe_list': recipe_list, 'user': name, 'user_id': request.session['user_id'], 'action': "nutriLink:logout", 'actionMessage': "Log Out"}
    else:
        context = {'recipe_list': recipe_list, 'action': "nutriLink:sign_in", 'actionMessage': "Sign In"}
    return HttpResponse(templete.render(context, request))


def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    try:
        selected_recipe = Recipe.objects.get(pk=request.POST["choice"])
    except (KeyError, Recipe.DoesNotExist):
        return render(
            request,
            "nutriLink/recipe.html",
            {
                'recipe': recipe,
                'error_message': "You didn't select a choice.",
            },
        )
    else:
        return HttpResponseRedirect(reverse("nutriLink:results", args=(selected_recipe.id,)))


def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, "nutriLink/user.html", {'user': user, 'user_id': user_id})


def recipe_form(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404('User does not exist')  # NIEZSLOGOWANY UŻYTKOWNIK
    return render(request, "nutriLink/recipe_form.html", {'user': user})


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


def new_recipe(request, user_id):
    form = RecipeForm(request.POST or None)
    return render(request, 'nutriLink/recipe_form.html', {"form": form, 'user_id': request.session["user_id"]})


def insert_recipe(request, user_id):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe_name = request.POST['recipe_name']
            contents = request.POST['contents']
            picture = request.POST['picture']
            pub_date = request.POST['pub_date']
            new_recipe = Recipe(recipe_name=recipe_name, contents=contents, picture=picture, pub_date=pub_date, user_id=request.session["user_id"])
            new_recipe.save()
            return render(request, 'nutriLink/recipe_form.html', {"form": form, "message": "New recipe added successfully",'user_id': request.session["user_id"]})
        else:
            return render(request, 'nutriLink/recipe_form.html', {"form": form, "message": "Insert valid recipe details",'user_id': request.session["user_id"]})


def logout(request):
    if request.session["user_id"] != "":
        del request.session['user_id']