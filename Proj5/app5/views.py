from django.shortcuts import render

def showIndex(request):
    d1 = {
        "idno":101,
        "name":"Ravi",
        "salary":185000.00
    }
    return render(request,"index.html",{"emp":d1})