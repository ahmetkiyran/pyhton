"""sayılar = [1,3,5,7,9,12,19,21]

# sayılar listesindeki hangi sayılar 3 ün katıdır?
for i in sayılar:
    if(i%3 == 0):
        print(i)
# sayılar listesindeki sayıların toplamı kaçtır?
toplam = 0
for i in sayılar:
    toplam += i
print(f"sayıların toplamı: {toplam}")           

# sayılar listesindeki tek sayıların karesini alınız.
for i in sayılar:
    if(i%2 != 0):
        print("{i} nin karesi = " ,i**2) 

sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

# sehirlerden hangileri en fazla 5 karakterlidir?

for i in sehirler:
    if(len(i)<=5):
        print(i)  

urunler = [
    {"name" : "samsung s6", "price" : "3000"},
    {"name" : "samsung s7", "price" : "4000"},
    {"name" : "samsung s8", "price" : "5000"},
    {"name" : "samsung s9", "price" : "6000"},
    {"name" : "samsung s10", "price" : "7000"}
]              

#ürünlerin fiyatları toplamı nedir ?
toplam = 0
for urun in urunler:
    fiyat = int(urun["price"])
    toplam += fiyat
print(toplam)    

# urunlerden fiyatı en fazla 5000 olan ürünleri gosteriniz
int(urun["price"])
for urun in urunler:
    if(int(urun["price"])<= 5000):
        print(urun["name"])
        """
    