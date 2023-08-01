from django.shortcuts import render,HttpResponse
from django.contrib import messages
from employee.models import *
from . models import Contact

# Create your views here.
def index(request):
   return render(request,'mainproj/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
             messages.error(request, "Please enter your correct information!.")
        else:
            contact = Contact(name = name, email = email, phone=phone,desc = desc)
            contact.save()
            messages.success(request, "Your from has been done.")      
    return  render (request,'mainproj/contact.html')


def about(request):
    return render(request,'mainproj/about.html')


def search(request):
    query = request.POST.get('search')
    if len(query)>50: 
        messages.error(request, "Please enter your correct search!.")
    else:
        fname = Employee.objects.filter(first_name__icontains = query)
        lname = Employee.objects.filter(last_name__icontains = query) 
        all_emp = fname.union(lname)
    if all_emp.count()==0:
        messages.warning(request, "Please enter relevent search information!.")    
    param = {"allemp":all_emp} 
    return render(request,'mainproj/search.html',param)

    

