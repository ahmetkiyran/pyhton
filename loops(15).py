"""
 for döngüsü

 *** in operatörü aradığımız değerin o liste sözlük veya arrayde olup olmadığını 
 kontrol eden bir operatördür.

 
liste = [1,2,3,4,5]

print(5 in liste)

liste1 = [1,2,3,4,5,6,7]

for eleman in liste1:
    print(eleman)

toplam = 0

for eleman in liste1:
    toplam += eleman
    print(toplam)
print(toplam)

liste2 = [1,2,4,5,6,8,10,24,46]
for eleman in liste2:
    if eleman %2 == 0:
        print(eleman)


s = "python"
for i in s:
    print(i)
    """

# while döngüsü

i = 0
while(i<5):
    print("i nin değeri: ",i)
    i+=1

i = 0
while(i<5):
    print("adınızı giriniz: ")
    i+=1

# range fonksiyonu


print(*range(0,20))

print(*range(1,20))

print(*range(1,100,2))# en sonda atlama değerini girdik


print(*range(20,0,-1)) #tersten bastır

for i in range(10):
    print(i)


# break ve continue ifadeleri

for i in range(10):
    if i == 5:
        break
    else:
        print(i)   

for i in range(10):
    if i == 5:
        continue
    else:
        print(i)  