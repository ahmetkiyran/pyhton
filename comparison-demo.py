# girilen 2 sayıdan hangisi büyüktür? 



"""a = int(input("bir sayı giriniz: "))
b = int(input("bir sayı giriniz: "))

result = (a>b)
print(f'a: {a} değeri b: {b} den büyüktür {result}')"""

# kullanıcıdan 2 vize(%60) ve final (%40) notunu alıp ortalama hesaplayınız
#eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırırnız

"""vize1 = float(input("1. vize: "))
vize2 = float(input("2.vize: "))
final = float(input50("final: "))

ortalama= ((vize1 +vize2)/2)*(0.6)+(final*0.4)

print(f"not ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama>=50}")"""

#girilen sayının tek mi çift mi olduğunu yazdırınız

"""sayı = int(input("sayı giriniz: "))

tekcift = (sayı % 2 == 0)

print(f"girilen sayının çift olma durumu : {tekcift}")"""

#girilen sayının pozitif mi negatif mi olduğunu bulun

"""sayı = int(input("sayı: "))

negatifpozitif = (sayı > 0)

print(f"girilen sayının pozitif olma durumu : {negatifpozitif}")"""

# parola ve mail bilgisini isteyip doğruluğunu kontrol ediniz.
 # email: ahmet.kiyran1@gmail.com parola: 79747938
 
email ="ahmet.kiyran1@gmail.com"
password  ="79747938"

girEmail= input("email: ")
girPassword = input("parola: ")

isEmail = (email == girEmail)
isPassword=(password == girPassword)

print(f"email bilgisi: {isEmail} ve parola bilgisi: {isPassword}")
