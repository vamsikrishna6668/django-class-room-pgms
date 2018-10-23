from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")

def validate(request):
    uname = request.POST.get("t1")
    upass = request.POST.get("t2")

    from firebase import firebase as fab
    fa = fab.FirebaseApplication("https://djangoweb1.firebaseio.com/admin/login",None)
    d1 = fa.get("login/",None)

    if d1["username"] == uname and d1["password"] == upass:
        return render(request,"welcome.html")
    else:
        print("Invalid")
        d = {"message":"Invalid User"}
        return render(request,"index.html",d)
