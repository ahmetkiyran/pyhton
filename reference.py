# value types -> string, number
x = 5
y = 25

x = y

y = 10

#print(x,y)

#reference types => list

a = ["apple","banana"]
b = ["apple","banana"]

a = b# aynı adresi gösterdiğinden dolayı b de yapılan değişiklik ikisini de etkiler.

b[0] = "grape"

print(a,b)

# value type larda verinin kendisiyle reference typelarda verinin adresiyle ilgileniriz.
