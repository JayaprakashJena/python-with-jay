from django.shortcuts import render

def showIndex(request):

    return render(request,'index.html',{"name":"jay","salary":12000})
