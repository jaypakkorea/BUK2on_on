from django.shortcuts import render
from .models import Restaurant


# Create your views here.
def index(request):
    recommends = Restaurant.objects.all()
    print(recommends)
    context ={
        'recommends' : recommends,
    }
    return render(request, "recommends/index.html", context)


def detail(request, restaurant_pk ):
    recommend = Restaurant.objects.get(pk=restaurant_pk)

    context = {
        'recommend' : recommend,
    }
    return render(request, 'recommends/detail.html', context)