from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context={
        "variable1":"this is nandini trial,",
        "variable2":"trial is okay"
    }
    return render(request,'index.html')
    #return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is aboutpage")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is servicespage")

def contact(request):
    return render(request,'contact.html')
    #return HttpResponse("this is contactpage")