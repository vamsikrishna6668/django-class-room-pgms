from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def showDetails(request):
    name = request.POST.get("t1")
    age = request.POST.get("t2")
    cno = request.POST.get("t3")
    email = request.POST.get("t4")
    salary = request.POST.get("t5")
    address = request.POST.get("t6")

    d1 = {
        "name":name,
        "age":age,
        "cno":cno,
        "email":email,
        "sal":salary,
        "adds":address
    }
    return render(request,"details.html",d1)