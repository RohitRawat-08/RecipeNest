from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from BaseApp.forms import RecipeForm
from BaseApp.models import Recipe

# Create your views here.

@login_required(login_url='home')
def home(request):

    Recipes = Recipe.objects.all()
    context={"data":Recipes}

    return render (request , "home.html",context)



@login_required(login_url='home')
def add_recipe(request):
    if request.method=="POST":
        f=RecipeForm(request.POST)
        if f.is_valid():
            recipe = f.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('home')

        # print(RecipeForm.author)

    context={"form":RecipeForm}


    return render (request , "add_recipe.html",context)


@login_required(login_url="home")
def your_recipe(request):
    recipe_data = Recipe.objects.filter(author = request.user)
    context={"data":recipe_data}

    return render(request , "your_recipe.html",context)

@login_required(login_url=home)
def edit(request,id):
    data = Recipe.objects.get(id=id)

    if request.method == "POST":
        title = request.POST['title']
        ing = request.POST['ingredients']
        ins = request.POST['instruction']
        cat = request.POST['catrgory']
        # print(title,ing,ins,cat)
        data.title = title
        data.ingredients = ing
        data.instruction = ins
        data.catrgory = cat
        data.save()
        return redirect('home')
    
    context = {"form":data}
    # else:
    #     context = {"form":RecipeForm}
        

    return render(request ,"edit.html",context)

@login_required(login_url='home')
def delete(request,id):
    data = Recipe.objects.get(id=id)
    data.delete()
    return redirect('your_recipe')




def Profile(request):

    return render(request , 'profile.html')
