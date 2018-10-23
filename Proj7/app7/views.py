from django.shortcuts import render
from firebase import firebase as fab

def showIndex(request):
    fb = fab.FirebaseApplication("https://djangoweb1.firebaseio.com/admin/login",None)
    d1 = fb.get("login/",None)

    fb1 = fab.FirebaseApplication("https://djangoweb1.firebaseio.com/admin/student", None)
    d2 = fb1.get("student/", None)

    d3 = {"login":d1,"student":d2}

    return render(request,"index.html",{"admin":d3})

