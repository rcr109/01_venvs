from django.shortcuts import render


def My_Home(request):
    return render(request, "home/home.html")
