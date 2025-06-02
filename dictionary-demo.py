"""ogrenciler = {
    "120" : {
        "ad": "ali",
        "soyad": "yılmaz",
        "telefon": "532 000 00 01"
    },
    "125": {
        "ad": "can",
        "soyad": "korkmaz",
        "telefon":"532 000 00 02"
    },
     "128": {
        "ad": "volkan",
        "soyad": "yükselen",
        "telefon":"532 000 00 03"
    },
    
}
1- bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
2- öğrenci numarasını kullanıcıdan alıp ilgili öğrenci biligisini gösterin





"""
ogrenciler = {}
number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

ogrenciler[number] = {
    "ad": name,
    "soyad" : surname,
    "telefon": phone
}

print(ogrenciler)