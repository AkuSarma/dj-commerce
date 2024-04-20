from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_store, name="home=store"),
]
