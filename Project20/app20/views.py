from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def display(request):
    res = request.POST.get("course")
    return render(request,"index.html",{"course":res})