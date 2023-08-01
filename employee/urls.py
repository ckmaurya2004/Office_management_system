from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index , name= "index"),
    path("totalemp/",views.total_employee,name = "TOtalEmp"),
    path("addemp/",views.add_employee,name = "AddEMp"),
    path("removeemp/",views.remove_employee,name = "RemoveEmp"),
    path("removeemp/<int:myid>",views.remove_employee,name = "RemoveEmp"),
    path("filteremp/",views.filter_employee,name = "FIlteremp")


]