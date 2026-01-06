from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact


# Create your views here.
def index(request):
    context={
        "variable1":"this is nandini trial,",
        "variable2":"trial is okay"
    }
    return render(request,'index.html')
    #return HttpResponse("this is homepage")
    
def contact(request):
    if request .method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, email, phone, message)
        
    return render(request, 'index.html')

    
    

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is aboutpage")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is servicespage")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        
    return render(request,'contact.html')
    #return HttpResponse("this is contactpage")
    
