# key -> value
# 41 => kocaeli
# 34 => istanbul

"""sehirler = ["kocaeli","istanbul"]
plakalar = [41,34]

#print(plakalar[sehirler.index("istanbul")])

# print(plakalar["kocaeli"]) => 41
# print(plakalar["istanbul"]) => 34
#yapmak istediğimiz şey bu

plakalar = {"kocaeli" : 41, "istanbul" : 34}

print(plakalar["kocaeli"])

plakalar["ankara"] = 6
print(plakalar)"""

users = {
    "ahmetkiyran":{
        "age": 24,
        "email":"ahmet.kiyran1@gmail.com",
        "address": "konya",
        "phone": "74794972"
        
    },
    "mustafakiyran":{
        "age": 70,
        "email": "none",
        "adress": "osmaniye",
        "phone": "230842"
    }
}

print(users["mustafakiyran"]["age"])
