from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index , name= "index"),
    path("contact/",views.contact, name = "Contact"),
    path("about/",views.about, name = "about"),
    path("search/",views.search, name = "Search")


]