from django.shortcuts import render

def showIndex(request):
    employee_new={'data': 
           [{'idno':101,'class':'one','name':'jay','marks':[34,45,56,67,30]},
           {'idno':102,'class':'two','name':'naveen','marks':[34,45,56,67,40]},
           {'idno':103,'class':'three','name':'Raj','marks':[34,45,56,67,20]},
           {'idno':103,'class':'three','name':'Raj','marks':[34,45,56,'A',67]},
           {'idno':104,'class':'four','name':'Ravi','marks':[34,45,'A',56,67]},
           ]      
           }
    return render(request,'empnew_file.html',employee_new )

