# if blokları

a = int(input("bir yaşınızı giriniz: "))

if(a<18):
    print("mekana giremezsiniz.")
else:
    print("hoşgeldiniz...")

# if else elif

a = input("bir değer giriniz: (+,-,/,*)")

if a == "+":
    print("toplama")
elif a == "-":
    print("çıkarma işlemi")
elif a == "*":
    print("çarpma işlemi")
else:
    print("bölme işlemi")