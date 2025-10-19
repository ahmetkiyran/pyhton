
with open("bilgiler2.txt","r+") as file: # r+ hem okumayı hem de yazmayı sağlar.
    print(file.read())

"""with open("bilgiler2.txt","r+") as file: # r+ hem okumayı hem de yazmayı sağlar.
    file.seek(10)
    file.write("deneme")
    print(file.read())"""

# dosyanın sonunda değişiklik yapma

with open("bilgiler2.txt","r+") as file: # r+ hem okumayı hem de yazmayı sağlar.
     print(file.read())

with open("bilgiler2.txt","a") as file: # r+ hem okumayı hem de yazmayı sağlar.
     file.write("yağız eren olgun\n")
   
with open("bilgiler2.txt","r+") as file: # r+ hem okumayı hem de yazmayı sağlar.
     print(file.read())

#dosyanın başında değişiklik yapmak

with open("bilgiler2.txt","r+") as file: # r+ hem okumayı hem de yazmayı sağlar.
     icerik = file.read()
     icerik = "emir çalışır\n" + icerik
     print(icerik)

#dosyanın ortasında değişiklik yapmak
with open("bilgiler2.txt","r+") as file: # r+ hem okumayı hem de yazmayı sağlar.
     liste = file.readlines()
     print(liste)
     liste.insert(3,"samet yiğit\n")
     file.seek(0)
     file.writelines(liste)

with open("bilgiler2.txt","r+") as file: # r+ hem okumayı hem de yazmayı sağlar.
     print(file.read())