# dosyaları otomatik kapatma
"""
with open(dosya_adı,dosya_kipi) as file:
        dosya işlemleri

yaptığımızda dosyamız otomatik olarak kapanıyor.        
"""
with open("bilgiler.txt","r") as file:
    for i in file:
        print(i)

# dosyaları ileri geri sarmak

with open("bilgiler.txt","r") as file:
    print(file.tell())# dosya imlecinin nerede olduğunu bize söyler.
    file.seek(20)# dosyada imleci 20 ye götürdük
    print(file.tell())

with open("bilgiler.txt","r") as file:
    file.seek(5)#dosyayı 5. karaktere götürdük
    icerik = file.read(10)#5 ten sonra 10 karakteri okuduk
    print(icerik)# yazdırdık

with open("bilgiler.txt","r") as file:
    file.seek(5)#dosyayı 5. karaktere götürdük
    icerik = file.read(10)#5 ten sonra 10 karakteri okuduk
    print(file.tell())
    print(icerik)# yazdırdık