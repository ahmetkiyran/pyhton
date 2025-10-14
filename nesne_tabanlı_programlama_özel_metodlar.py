"""class Kitap():
    pass"""

"""kitap = Kitap() # python burda _init_ metodunu çağırıyor.

print(kitap) # python burda str metodunu tanımlıyor

print(len(kitap)) # python burda len metodunu çağırmak istiyor ama bulamıyor"""

class Kitap():
    def __init__(self,isim,yazar,sayfa,tür):
        print("init fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa = sayfa
        self.tür = tür

kitap = Kitap("istanbul hatırası","Ahmet ümit",561,"polisiye")

print(kitap)

class Kitap():
    def __init__(self,isim,yazar,sayfa,tür):
        print("init fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa = sayfa
        self.tür = tür
    def __str__(self):
        return "isim :  {}\nYazar: {}\nSayfa Sayısı: {}\nTürü: {}".format(self.isim,self.yazar,self.sayfa,self.tür)
    
kitap = Kitap("istanbul hatırası","Ahmet ümit",561,"polisiye")

print(kitap)

class Kitap():
    def __init__(self,isim,yazar,sayfa,tür):
        print("init fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa = sayfa
        self.tür = tür
    def __str__(self):
        return "isim :  {}\nYazar: {}\nSayfa Sayısı: {}\nTürü: {}".format(self.isim,self.yazar,self.sayfa,self.tür)
    def __len__(self):
        return self.sayfa
kitap = Kitap("istanbul hatırası","Ahmet ümit",561,"polisiye")

print(len(kitap))

class Kitap():
    def __init__(self,isim,yazar,sayfa,tür):
        print("init fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa = sayfa
        self.tür = tür
    def __str__(self):
        return "isim :  {}\nYazar: {}\nSayfa Sayısı: {}\nTürü: {}".format(self.isim,self.yazar,self.sayfa,self.tür)
    def __len__(self):
        return self.sayfa
    def __del__(self):
        print("kitap objesi siliniyor...")

del kitap

print(kitap)