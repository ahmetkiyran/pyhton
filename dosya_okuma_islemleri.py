# dosyaları okumak için r kipiyle açarız dosyamızı
# eğer dosyayı bulamazsa FileNotFoundError hatası döndürecek.

file= open("bilgiler.txt","r")

# for döngüsü ile dosya okumak

file= open("bilgiler.txt","r")

for i in file:
    print(i)

file.close()

#read() fonksiyonu ile okumak

file = open("bilgiler.txt","r")
icerik = file.read()
print("dosyanın içeriği: ")

print(icerik)
file.close()

# readline fonksiyonu 

# her çalıştırıldığında dosyanın sadece bir satırını okur

file = open("bilgiler.txt","r")
print(file.readline())
file.close()

# readlines fonksiyonu
# dosyanın bütün satırlarını bir liste şeklinde döndürür.

file = open("bilgiler.txt","r")
print(file.readlines())
file.close()