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