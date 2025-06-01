#"bmw, mercedes, opel, mazda" elemanlarına sahip bir liste oluşturunuz.

cars = ["bmw","mercedes","opel","mazda"]
print(cars)

# liste kaç elemanlıdır

print(len(cars))

# listenin ilk ve son elemanı nedir

print(cars[0])
print(cars[3])

# mazda değerini toyota ile değiştir

cars[-1] = "toyota"
print(cars)

# mercedes listenin bir elemanı mıdır?

a = "mercedes" in cars
print(a)

# listenin -2 indeksindeki değer nedir ?

print(cars[-2])

# listenin ilk üç elemanını alın

print(cars[0:3])

#listenin son iki elemanı yerine "toyota" ve "renault" değerlerini ekleyin

cars[-2:] = ["toyota","renault"]
print(cars)

# listenin üzerine "audi" ve "nissan" değerlerini ekleyin

cars += ["audi","nissan"]
print(cars)

# listenin son elemanını silin

del cars[-1] # del silme fonksiyonudur.
print(cars)

#liste elemanlarını tersten yazdırın

print(cars[::-1])

# aşağıdaki verileri bir liste içinde saklayınız

    #studentA: Yiğit Bilgi 2010,(70,60,70)
    #studentB: Sena Turan 1999,(80,80,70)
    #studentC: Ahmet Turan 1998,(80,70,90)
    
studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]

students = studentA+studentB+studentC

a = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2]/3)}" 


print(a)
