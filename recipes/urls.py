from django.urls import path

from recipes.views import myhome, recipes

urlpatterns = [
    path("receitas/", recipes),
    path("", myhome),
]
