from re import M


fruits = {"orange","apple","banana"}

#print(fruits[0]) indekslenemez

for x in fruits:
    print(x)

fruits.add("cherry") 
   
print(fruits)

fruits.update(["mango","grape","apple"])
print(fruits)

# sets de bir eleman listede varken aynısını tekrar eklemek istersek bu yapılamaz

# myList = [1,2,3,4,5,4,3,4,5,6]

# print(myList) #listeyi olduğu gibi yazar
# print(set(myList)) #set fonksiyonu sayesinde listede tekrar eden değerleri teke düşürür

fruits.remove("mango")
fruits.discard("apple")

print(fruits)

fruits.pop()
#fruits.clear() -> bütün elemanları siler
print(fruits)

