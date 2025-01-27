from django.shortcuts import redirect,render
from BaseApp.models import Recipe
from django.db.models import Q

def search(request):
    no_data_found = False
    if request.method == 'GET':
        if 'search' in request.GET:
            s_data = request.GET['search']
            # print(s_data)

            f_data = Recipe.objects.filter(Q(title__icontains = s_data) | Q(catrgory__icontains=s_data))

            if len(f_data) == 0:
                no_data_found = True

    context={"data":f_data , 'noMatch':no_data_found}

    return render(request ,"home.html",context)

