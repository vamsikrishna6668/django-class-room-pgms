from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def display(request):
    name = request.POST.get("fname")
    return render(request,"index.html",{"fname":name})