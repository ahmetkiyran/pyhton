


x,y,z = 2,5,107

numbers = 1,5,7,10,6

# kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?

"""a = int(input(" sayı giriniz: "))
b = int(input("bir sayı giriniz: "))

sonuc = (a * b)- (x+y+z)
print(sonuc)"""

# y nin x e kalansız bölümünü hesaplayınız.

"""bolum = y/x
print(bolum)"""

# (x,y,z) toplamının mod 3 ü nedir

"""toplam = x+y+z 
sonuc = toplam%3
print(sonuc)"""

# y nin x inci kuvvetini hesaplayınız

"""sonuc = y ** x
print(sonuc)"""

# x, *y , z = numbers işlemine göre z nin küpü nedir

"""x , *y ,z = numbers
sonuc = z ** 3
print(sonuc)"""

#x, *y , z = numbers işlemine göre y nin değerleri toplamı nedir
numbers = 1,5,7,10,6
x , *y, z = numbers
sonuc = y[0]+y[1]+y[2]

print(sonuc)