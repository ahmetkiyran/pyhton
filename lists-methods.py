from numpy import number


numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','S']

val = min(numbers) # min değeri bulur
print(val)
val = max(numbers) # max değeri bulur
print(val)

val = max(letters)# max karakteri bulur
print(val)
val = min(letters)#min karakteri bulur
print(val)

val = numbers[3:6]# 3.indeksten 6 ya kadar alır
print(val)

val = numbers[:3]
print(val) #baştan 3 e kadar yazdırır

numbers[4] = 56
print(numbers) # dördüncü indeksteki elemanı değiştirdik

numbers.append(49) # append metodu listenin sonuna eleman ekler
print(numbers)

numbers.insert(3,78)#insert metodu belirlenen indisin yerine koyar
print(numbers)

# append yerine insert(-1) de liste sonuna ekleme yapar.

numbers.pop(0) # pop metodu belirtilen indisin listeden silinmesini sağlar
print(numbers)

numbers.remove(10) # remove komutu listede belirlenen elemanın kaldırılmasını sağlar
print(numbers)

numbers.sort()# listenin küçükten büyüğe göre sıralanmasını sağlar
print(numbers)

letters.sort()# listenin alfabetik olarak sıralanmasını sağlar.
print(letters)

numbers.reverse()#listeyi tam tersine çevirmeye yarar.
print(numbers)

numbers.clear()# listeyi silmeye yarar.
print(numbers)