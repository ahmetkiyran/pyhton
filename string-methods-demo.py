from unittest import result


website = "http://ahmetkiyran.com"
course = "Pyhton Kursu : Baştan Sona Python programlama rehberiniz (40 saat)"


# " hello world " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

"""result = " hello world ".strip()
print(result)

result = " hello world ".lstrip() #soldan silme
print(result)
result = " hello world ".rstrip() #sağdan silme
print(result)"""

# "www.ahmetkiyran.com" içindeki ahmetkiyran bilgisi haricindeki her karakteri silin.

"""result = "www.ahmetkiyran.com".strip("w.moc")# stripin içine hangilerini silmek istiyorsak karakterleri yazabiliriz. 
print(result)"""

# "course" karakter dizisinin tüm karakterlerini küçük harf yap

"""result = course.lower()
print(result)"""

# "website" içinde kaç tane a karakteri vardır

"""result = website.count("a")
print(result)"""

# "website" wwww ile başlayıp com ile bitiyor mu 

"""result = website.startswith("www")
print(result)
result = website.endswith("com")
print(result)"""

# "website" içerisinde .com ifadesi var mı 

"""result = website.count(".com")
print(result)"""

"""result = website.find(".com")
print(result)
"""


# "course" içindeki karakterlerin hepsi alfabetik mi

"""result = course.isalpha()
print(result)""" #sayısal değerler içerdiği için false döndürür.

"""result = "hello".isalpha()
print(result)"""

# isdigit() de sayısal kontrolü yapar

# "contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz

"""result = 'Contents'.center(50, '*')
print(result)

ljust veya rjust gibi ifadelerle de sağa ve sola yaslama yapabiliriz."""

# "course" karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştirin

"""result = course.replace(" ", "-")
print(result)"""

# "hello world" karakter dizisindeki world ü there olarak değiştir

"""result ="hello world".replace("hello", "there")
print(result)"""

# "course" karakter dizisini boşluk karakterlerinden ayırın

result = course.split(" ")
result = result[5]
print(result)
