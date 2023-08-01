from django.shortcuts import render,HttpResponse
from . models import Employee
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def index(request):
   return render(request,'employee/index.html')

def total_employee(request):
   all_emp = Employee.objects.all()
   param = {"allemp":all_emp} 

   return render(request,'employee/totalemp.html',param)

def add_employee(request):
   if request.method =="POST":
      first_name = request.POST['fname']
      last_name = request.POST['lname']
      phone = request.POST['phone']
      role = request.POST['role']
      dept = request.POST['dept']
      location = request.POST['location']
      bonus = request.POST['bonus']
      salary =request.POST['salary']
      new_emp = Employee(first_name = first_name, last_name = last_name, bonus = bonus, dept_name = dept,salary = salary, location = location,phone = phone, role_name= role)
      new_emp.save()
      messages.success(request,'Employee has been added successfully')
   else:
      messages.error(request, "Please enter your correct information!.")

   return render(request,'employee/addemp.html')

def remove_employee(request,myid=0):
   if myid:
      try:
         rem_emp = Employee.objects.get(id=myid)
         rem_emp.delete()
         messages.success(request,'Employee has been removed successfully')
  
      except :
         messages.error(request, "not removed employess!.")
    
   allemp = Employee.objects.all()
   param = {'allemp':allemp}
   return render(request,'employee/removeemp.html',param)

def filter_employee (request):
   if request.method == "POST":
      name = request.POST['name']
      role = request.POST['role']
      dept = request.POST['dept']
      emps= Employee.objects.all()
      if name:
         emps=emps.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
      if role:
         emps = emps.filter(role_name__icontains = role)
      if dept:
         emps = emps.filter(dept_name__icontains= dept)
      param = {'allemp':emps}
      return render(request,'employee/totalemp.html',param)
   elif  request.method=='GET': 
      return render(request,'employee/filteremp.html')
   else:
      messages.error(request, "not match employee's detail sorry please try again!.")


