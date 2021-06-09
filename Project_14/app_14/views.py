from django.shortcuts import render

def showIndex(request):
    return render(request,'index.html')
def loginCheckout(request):
    Username=request.POST.get("t1")
    password=request.POST.get("t2")
    if Username == 'jay' and password =='jay123' :
        return render(request,"welcome.html")
    else:
        return render(request,"error.html")