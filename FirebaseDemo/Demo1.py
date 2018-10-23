from firebase import firebase as fab
fa = fab.FirebaseApplication("https://djangoweb1.firebaseio.com/",None)
d1 = fa.get("",None)

for a,b in d1.items():
    print(a)
    for c,d in b.items():
        print(c)
        for e,f in d.items():
            print(e)
            for g,h in f.items():
                print(g)
                for i in h.values():
                    print(i,end="---")
                print()