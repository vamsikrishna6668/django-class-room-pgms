from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def showDetails(request):
    na = request.POST.get("t1")
    ag = request.POST.get("t2")
    cn = request.POST.get("t3")

    d1 = {"name":na,"age":ag,"cno":cn}

    return render(request,"details.html",d1)
