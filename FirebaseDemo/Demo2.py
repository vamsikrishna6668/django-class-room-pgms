from firebase import firebase as fab
fa = fab.FirebaseApplication("https://djangoweb1.firebaseio.com/")
d1={"login":{"username":"python","password":"sathya"}}
fa.put("https://djangoweb1.firebaseio.com/","admin",d1)
print("Data Saved")
