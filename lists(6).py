# stringler değiştirilemez ama listeler değiştirilebilir.

liste= ["elma",15,"armut",3]
print(type(liste))
print(len(liste))
liste = list("merhaba") # listedeki elemanı stringe çeviriyor.
print(liste)
print(len(liste))

liste2 = [1,2,3,4,5,6,7,8]
print(liste2[3]) # arrayde eleman yazdırma gibi burda da yapabiliyoruz.
print(liste2[-1]) # sondaki elemana erişmek için yine -1 yazmak yeterli 

# listelerde parçalama
print(liste2[4:])
print(liste2[:5])
print(liste2[::2])
print(liste2[::-1])

# liste birleştirme

liste3 = [1,2,3,4]
liste4 = [5,6,7,8]
liste5 = liste3 + liste4
print(liste5)
print(liste3 *3)

#listelerde eleman değiştirme
print(liste5)
liste5[3] = 23
print(liste5)

#listede metotlar
liste5.append(96) # listenin sonuna eleman eklememizi sağlar.
print(liste5)
liste5.pop() # içine bir değer vermediğimizde listenin sonundaki elemanı listeden atar.
print(liste5)
liste5.pop(0)# içine atmak istediğimiz değerin indeks numarasını vermemiz lazım.
print(liste5)

liste6 = [35,3,4,78,65,42]
liste6.sort() # listeyi büyükten küçüğe doğru sıralamamızı sağlar.
print(liste6)
liste6.sort(reverse= True)# tersten sıralamamızı sağlar.
print(liste6)
#iç içe listeler
liste = [[8,9,56],[23,45,7],[12,22,45,67]]
print(liste)