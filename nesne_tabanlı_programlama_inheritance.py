# bir sınıfın başka bir sınıftan özellikleri veya metodları miras almasıdır.

class Calisan():

    def __init__(self,isim,maaş,departman):
        print("çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.maaş = maaş
        self.departman =departman
    def bilgileriGoster(self):
        print("çalışan sınıfının bilgileri ....")

        print("isim: {}\nMaaş: {}\nDepartman: {}\n".format(self.isim,self.maaş,self.departman))

    def departman_degistir(self,yeni_departman):
        self.departman = yeni_departman

class Yönetici(Calisan):
    def zamyap(self,zam_mikarı):
        self.maaş += zam_mikarı 

yönetici = Yönetici("ahmet",2000,"bilişim")
print(yönetici)
print(yönetici.bilgileriGoster())
yönetici.departman_degistir("güvenlik")
print(yönetici.bilgileriGoster())

yönetici = Yönetici("ahmet",2000,"bilişim")
yönetici.zamyap(500)
print(yönetici.bilgileriGoster())
#overriding

# eğer biz miras aldığımız metodları aynı isimle kendi sınıfımızda tekrar tanımlarsak,artık metodu çağırdığımız 
# zaman miraz aldığımız değil kendi metodumuz çalışacaktır
#buna da nesne tabanlı programlamada metodu override etmek denmektedir.

class Calisan():

    def __init__(self,isim,maaş,departman):
        print("çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.maaş = maaş
        self.departman =departman
    def bilgileriGoster(self):
        print("çalışan sınıfının bilgileri ....")

        print("isim: {}\nMaaş: {}\nDepartman: {}\n".format(self.isim,self.maaş,self.departman))

    def departman_degistir(self,yeni_departman):
        self.departman = yeni_departman

class Yönetici(Calisan):
    def __init__(self, isim, maaş, departman,kişi_sayısı):
        print("yönetici sınıfının init fonksiyonu...")
        self.isim = isim
        self.maaş = maaş
        self.departman =departman
        self.kişi_sayısı = kişi_sayısı

    def bilgileriGoster(self):
        print("yönetici sınıfının bilgileri ....")
        print("isim: {}\nMaaş: {}\nDepartman: {}\nSorumlu kişi sayısı: {}\n".format(self.isim,self.maaş,self.departman,self.kişi_sayısı))
    def zamyap(self,zam_mikarı):
        self.maaş += zam_mikarı 

yönetici = Yönetici("bulut",2000,"bilişim",6)

print(yönetici.bilgileriGoster())
#super anahtar kelimesi

"""
super anahtar kelimesi özellikle override ettiğimiz bir metodun
içinde aynı zamanda miras aldığımız bir metodu kullanmak istersek kullanılabilir.
yani super en genel anlamıyla miras aldığımız sınıfın metodlarını alt sınıflardan kullanmamızı sağlar.
"""

class Calisan():

    def __init__(self,isim,maaş,departman):
        print("çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.maaş = maaş
        self.departman =departman
    def bilgileriGoster(self):
        print("çalışan sınıfının bilgileri ....")

        print("isim: {}\nMaaş: {}\nDepartman: {}\n".format(self.isim,self.maaş,self.departman))

    def departman_degistir(self,yeni_departman):
        self.departman = yeni_departman

class Yönetici(Calisan):
    def __init__(self, isim, maaş, departman,kişi_sayısı):
        
        super().__init__(isim,maaş,departman)
        print("yönetici sınıfının init fonksiyonu...")

        self.kişi_sayısı = kişi_sayısı

    def bilgileriGoster(self):
        print("yönetici sınıfının bilgileri ....")
        print("isim: {}\nMaaş: {}\nDepartman: {}\nSorumlu kişi sayısı: {}\n".format(self.isim,self.maaş,self.departman,self.kişi_sayısı))
    def zamyap(self,zam_mikarı):
        self.maaş += zam_mikarı 

yönetici =Yönetici("ahmet",3000,"biişim",5)
print(yönetici.bilgileriGoster())
