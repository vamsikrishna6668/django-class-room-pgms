from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")


def registerNew(request):
    id = request.GET.get("update_id")
    from firebase import firebase as fab
    fire = fab.FirebaseApplication("https://djangoweb1.firebaseio.com/Employee", None)
    if id == None:
        d1 = fire.get("Employee/",None)
        key = 0
        if d1 == None:
            key = 101
        else:
            for x in d1:
                key = x
        key = (int(key)+1)
        return render(request,"register.html",{"key":key})
    else:
        d1 = fire.get("Employee/",id)
        return render(request,"register.html",{"key":id,"name":d1["name"],"cno":d1["contact"]})
def viewsAll(request):
    from firebase import firebase as fab
    fire = fab.FirebaseApplication("https://djangoweb1.firebaseio.com/Employee",None)
    d1 = fire.get("Employee/",None)
    return render(request,"views.html",{"emp":d1})


def saveDetails(request):
    id = request.POST.get("idno")
    name = request.POST.get("uname")
    contact = request.POST.get("cno")
    d1 = {"name":name,"contact":contact}
    from firebase import firebase as fab
    fire = fab.FirebaseApplication("https://djangoweb1.firebaseio.com/",None)
    fire.put("Employee/",id,d1)
    return render(request,"index.html")


def deleteDetails(request):
    id = request.POST.get("delete_id")
    from firebase import firebase as fab
    fire = fab.FirebaseApplication("https://djangoweb1.firebaseio.com/Employee", None)
    fire.delete("Employee/",id)
    return viewsAll(request)