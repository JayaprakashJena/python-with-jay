from django.shortcuts import render
from django.http import HttpResponse

def showMainPage(request):
    return render(request,'main.html')
def showRegisterPage(request):
    if request.method == "POST":
         n = request.POST.get('name')
         L=request.POST.get('Location')
         E=request.POST.get('Email')
         p=request.POST.get('password')
         return HttpResponse('ok')

    else:
        return render(request,'register.html')

def showAngular(request):
    return render(request,'angular.html')

def loginPage(request):
    return render(request,'login.html')