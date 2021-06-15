from django.shortcuts import render

def showIndex(request):
    employee={'data': 
           [{'idno':101,'class':'one','name':'jay','cno':358284667},
           {'idno':102,'class':'two','name':'naveen','cno':358284667},
           {'idno':103,'class':'three','name':'Raj','cno':358284667},
           {'idno':103,'class':'three','name':'Raj','cno':358284667},
           {'idno':104,'class':'four','name':'Ravi','cno':358284667},
           ]      
           }
    return render(request,'emp_file.html',employee )
