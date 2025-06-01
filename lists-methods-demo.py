names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

# Cenk ismini listenin sonuna ekleyin
names.append("Cenk")
print(names)
#Sena değerini listenin başına ekleyiniz
names.insert(0,"Sena")
print(names)

# deniz ismini listeden siliniz
del names[4]
print(names)

#ali listenin bir elemanı mıdır

a = "Ali" in names
print(a)

# liste elemanlarını ters çevirin
names.reverse()
print(names)

#liste elemanlarını alfabetik sıralayınız
names.sort()
print(names)

#years listesini rakamsal büyüklüğe göre sıralayınız

years.sort()
print(years)

#str = "chevrolet,dacia" karakter dizisini listeye çeviriniz
str = "chevrolet,dacia"
b = str.split(",")
print(b)

#years dizisinin min ve max değeri nedir

min = min(years)
print(min)
max = max(years)
print(max)

#years dizisinde kaç tane 1998 değeri vardır

c=years.count(1998)
print(c)

# years dizisinin tüm elemanlarını siliniz

years.clear()
print(years)



