#kullanıcıadi: ahmet@ktun.edu.tr
#sifre: 12345a12

kullanıcıAdi = input("kullanıcı adınızı giriniz: ")
sifre = input("şifrenizi giriniz: ")

if(kullanıcıAdi == "ahmet@ktun.edu.tr" and sifre == "12345a12"):
    print("giriş başarılı...")
elif(kullanıcıAdi == "ahmet@ktun.edu.tr" and sifre != "12345a12"):
    print("şifre hatalı")
elif(kullanıcıAdi != "ahmet@ktun.edu.tr" and sifre == "12345a12"):
    print("kullanıcı adı hatalı")
else:
    print("kullanıcı adı ve şifre hatalı")    