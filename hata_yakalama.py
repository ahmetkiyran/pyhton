"""

try except bloklarının yapısı şu şekildedir.

try:

hata çıkarabilecek kodlar buraya ayzılıyor
eğer hata çıkarsa program uygun olan except bloğuna girecek
hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak

except hata1:
hata1 oluştuğunda burası çalışacak
except hata2:
hata2 oluştuğunda burası çalışacak
"""




try:
    a = int("bdskndckbcdb3379")
    print(a)
    print("program burada")
except:
    print("bir hata oluştu")
print("bloklar sona erdi!")


try:
    a = int("3379")
    print(a)
    print("program burada")
except:
    print("bir hata oluştu")
print("bloklar sona erdi!")

try:
    a = int(input("sayı 1: "))
    b = int(input("sayı 2: "))
    print("cevap: ",a/b)
except ValueError:
    print("lütfen inputu doğru girin. ")
except ZeroDivisionError:
    print("bir sayı sıfıra bölünemez. ")
print("bloklar sona erdi. ")

#finally blokları
#mutlaka çalışması gereken kodların bulunması gerkeen bloklar
#hata olsa da olmasa da çalışması gerek
try:
    a = int(input("sayı 1: "))
    b = int(input("sayı 2: "))
    print("cevap: ",a/b)
except ValueError:
    print("lütfen inputu doğru girin. ")
except ZeroDivisionError:
    print("bir sayı sıfıra bölünemez. ")
finally:
    print("burası çalıştı...")
print("bloklar sona erdi. ")

#hata fırlatma

def terscevir(s):
    if(type(s) != str):
        raise ValueError("lütfen bir string değer giriniz!")
    else:
        return s[::-1]
    
    
try:
    print(terscevir(12))
except ValueError:
    print("fonksiyon hata verdi.")

#kendi fonksiyonlarımızda hata fırlatmayı bu şekilde yapabiliyoruz.