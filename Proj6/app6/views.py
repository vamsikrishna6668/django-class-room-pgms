from django.shortcuts import render

def showIndex(request):
    d1 = {
        "101" : {"name":"Ravi","salary":185000.00},
        "102" : {"name":"kumar","salary":250000.00},
        "103": {"name": "mohan", "salary": 50000.00},
        "104": {"name": "Krish", "salary": 550000.00}
    }
    return render(request,"emp_details.html",{"emp":d1})