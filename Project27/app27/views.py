from django.shortcuts import render
from django.http import HttpResponse
import csv

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def createCSV(request):
    http = HttpResponse(content_type="text/csv")
    http['Content-Disposition'] = 'attachment; filename="employee.csv"'
    wr = csv.writer(http)
    wr.writerow([101,"Ravi","Developer",125000.00])
    wr.writerow([102,"kumar","Developer",185000.00])
    wr.writerow([103,"krish","TL",200000.00])
    return http
