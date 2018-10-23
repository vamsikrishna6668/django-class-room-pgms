from django.shortcuts import render
from .models import Product

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def saveProduct(request):
    no = request.POST.get("pno")
    name = request.POST.get("pname")
    price = request.POST.get("pprice")
    qty = request.POST.get("pqty")

    p1 = Product(_id=no,name=name,price=price,qty=qty)
    p1.save()

    return render(request,"index.html",{"response":"Product Saved"})