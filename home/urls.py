from django.urls import path

from home.views import My_Home

urlpatterns = [
    path("", My_Home),
]
