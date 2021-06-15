from django.http import request
from django.shortcuts import render

def showIndex(request):
    emp_info={'idno':101,'salary':150000.00,'names' :{'name_1':'jay','name_2':'Ajay','name_3':'Naveen'},'cno':'99456663','list_1':['apple','banana','mango',1100,220]}
    return render(request,'text_file.html',emp_info)
