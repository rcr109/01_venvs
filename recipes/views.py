from django.shortcuts import render


def recipes(request):
    return render(request, "recipes/pages/recipes.html",
                  context={'nome': '2023'})


def myhome(request):
    return render(request, "recipes/pages/home.html")
