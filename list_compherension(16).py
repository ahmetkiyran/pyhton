liste1 = [1,2,3,4,5,6]

liste2 = list()

for i in liste1:
    liste2.append(i)
print(liste2) # bu uzun yolu

liste3 = [3,4,5,6,7,8,9]
liste4 = [i for i in liste3]
print(liste4)