from django.shortcuts import render


def showIndex(request):
    return render(request,"index.html")


def dispay(request):
    date = request.POST.get("dob")
    return render(request,"index.html",{"dob":date})