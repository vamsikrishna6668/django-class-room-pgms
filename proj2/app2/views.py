from django.http import HttpResponse

def showHomePage(request):
    return HttpResponse("<H1>Hello Students</H1><h2>This is Django</h2>")