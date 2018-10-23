from django.http import HttpResponse

def showHomePage(request):
    return HttpResponse("Hello World I am the Home Page")
