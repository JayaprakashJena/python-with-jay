from django.shortcuts import render

def showInfo(request):
    return render(request,"file.html")