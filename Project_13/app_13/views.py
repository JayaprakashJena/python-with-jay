from django.shortcuts import render
from django.http import HttpResponse
def showIndex(request):
    return render (request,"index.html")
def showInit(request):
    Fname=request.POST.get("n1")
    Lname=request.POST.get("n2")
    full_name=Fname+" "+Lname
    return HttpResponse(full_name)
