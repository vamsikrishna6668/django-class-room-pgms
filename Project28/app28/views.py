from django.shortcuts import render
from .models import Employee
# Create your views here.
def showindex(request):
    return render(request,"index.html")


def saveDetails(request):
    name = request.POST.get("t1")
    cno = request.POST.get("t2")
    desig = request.POST.get("t3")
    sal = request.POST.get("t4")
    e = Employee(name=name,salary=sal,desingation=desig,cno=cno)
    e.save()
    return render(request,"index.html",{"status":"Details Saved"})


from django.http import HttpResponse

import csv

def downDetails(request):
    http = HttpResponse(content_type="text/csv")
    http['Content-Disposition'] = 'attachment; filename="employee.csv"'
    wr = csv.writer(http)

    res = Employee.objects.all()
    for x in res:
        wr.writerow([x.name,x.cno,x.desingation,x.salary])

    return http