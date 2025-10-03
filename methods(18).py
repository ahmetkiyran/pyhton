a = [1,2,3,4,5,6]
print(type(a))
a.append("python")
print(a)
# fonksiyonlar kod tekrarını azaltmaya yardım eder.
def selamla():
    print("merhaba")

selamla()
print(type(selamla))

def selamla(isim):
    print("isminiz: ",isim)

selamla("ahmet")

def toplama(a,b,c):
    print(a+b+c)

toplama(10,20,30)

# fonksiyonlarda retun ifadesi

"""def toplama(a,b,c):
    print("toplamları: ",a+b+c)

def ikiylecarp(a):
    print(a*2)
    bu iki fonksiyon arasında bağlantı kurulamaz çünkü return yok 
    """

def toplama(a,b,c):
    return a+b+c

def ikiylecarp(a):
    print(a*2)

toplam = toplama(3,4,5)
ikiylecarp(toplam)    

# fonksiyonlarda parametre türleri

def selamla(isim = "isimsiz"):
    print("selam",isim)

selamla()
#burdaki olay eğer biz fonksiyonun içine isim atamazsak otomatik kendisi
#isimsiz adında bir cevap veriyor 

def bilgilerigoster(ad = "bilgi yok",soyad = "bilgi yok",numara="bilgi yok"):
    print("ad: ",ad,"soyad: ",soyad,"numara: ",numara)

bilgilerigoster(numara=12345)# sadece belirtmek istediğimiz numaraysa böyle yazabiliriz.

# esnek sayılı değerler

def toplama(*a):
    print(a)

toplama(1,2,3,4,5)
toplama(1,2,3)
# burada tuple türüne dönüştürüyoruz ve bu sayede esneklik kazandırıyoruz.

def toplama(*a):
    toplam = 0
    for i in a:
        toplam += i
    print(toplam)
toplama(1,2,3,4)
toplama(1,2,3)

# global ve yerel değişkenler

def fonksiyon():
    a = 10
    print(a)
fonksiyon()
print(a)

#lambda ile fonksiyon oluşturma

def ikiylecarp(x):
    return x*2
print(ikiylecarp(3))

ikiylecarp = lambda x: x*2 #burdaki iki fonksiyon aynı 
