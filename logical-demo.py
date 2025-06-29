# girilen sayının 0-100 arasında olup olmadığını kontrol edin

"""x = int(input("sayıyı giriniz "))

result = x>= 0  and x < 100

print(result)"""

# girilen sayının sayının pozitif çift sayı olup olmadığını kontrol ediniz

"""x = int(input("sayıyı giriniz ")) 

result = x > 0 and  x % 2 == 0

print(result)"""

# email ve parola bilgileri ile giriş kontrolü yapınız.

"""girEmail = "ahmet.kiyran1@gmail.com"
girParola = "123456"

x = str(input("email giriniz: "))
y = str(input("parola giriniz: "))

result = girEmail == x and girParola == y

print(result)"""

# girilen 3 sayıyı büyüklük olarak karşılaştırınız

"""a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

result = a > b and b>c 
print(f'a en büyük sayıdır : {result}')"""

# kullanıcıdan 2 vize ve final notunu alıp ortalama hesaplayınız
 # eğer ortalama 50 ve üstüyse geçti yoksa kaldı yazdır
  # ortalama 50 olsa bile final notu en az 50 olmalıdır
  # finalden 70 alındığında ortalamanın önemi olmasın 
  
from re import A
from matplotlib.pylab import f


"""vize1 = float(input("vize1: "))
vize2 = float(input("vize2: "))
final = float(input("final: "))

ortalama = ((vize1 + vize2)/2)*0.6 + (final * 0.4)

#result = (ortalama >= 50) and (final >= 50)

result = (ortalama >= 50) or (final >= 50)
"
print(f'öğrencinin ortalaması {ortalama} ve geçme durumu: {result}')""",

# kişinin ad,kile ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
 #formül: kilo / boy uzunluğunun karesi
 # 0-18.4 = zayıf 18.5 - 24.9 = normal 25.0 - 29.9 = fazla kilolu 30.0 - 34.9  = şişman
 
name = str(input("adınız: "))
kg = float(input("kilonuz: "))
hg = int(input("boyunuz: "))

index = (kg)/ hg ** 2

zayıf = (index >= 0 ) and index <= 18.4
normal = index <18.4 and index <= 24.9
kilolu = index > 24.9 and index <= 29.9
obez = index >= 29.9 and index <=34.9

print(f'{name} kilo indexin: {index} ve kilo değerlendirmen zayıf :{zayıf}')
print(f'{name} kilo indexin: {index} ve kilo değerlendirmen normal :{normal}')
print(f'{name} kilo indexin: {index} ve kilo değerlendirmen kilolu :{kilolu}')
print(f'{name} kilo indexin: {index} ve kilo değerlendirmen obez :{obez}')
