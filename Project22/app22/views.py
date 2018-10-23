from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def display(request):
    value = request.POST.get("lang")
    return render(request,"index.html",{"lang":value})


def displayMulti(request):
    li = request.POST.getlist("langs")
    return render(request,"index.html",{"langs":li})