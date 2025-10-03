print("kullanıcı giriş programı")

kullanıcı_adi = "ahmet"
sifre = "12345"
giris_hakki = 3
while True:
    kullanıcıAdi = input("kullanıcı adınızı giriniz: ")
    parola = input("şifrenizi giriniz: ")
    if kullanıcı_adi !=kullanıcıAdi and sifre == parola:
        print("kullanıcı adı hatalı...")
        giris_hakki -= 1
    elif kullanıcı_adi == kullanıcıAdi and sifre != parola:
        print("sifre hatalı")
        giris_hakki -= 1
    elif kullanıcı_adi != kullanıcıAdi and sifre != parola:
        print("kullanıcı adı ve parola hatalı")
        giris_hakki -= 1
    else:
        print("sisteme giriş yapıldı")    
        break
    if giris_hakki == 0:
        print("giriş hakkınız bitti")
        break