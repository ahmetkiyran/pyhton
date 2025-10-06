"""
sınıflar veya classlar objelerimizi oluştururken
objelerin özelliklerini ve metodlarını tanımadığımız
bir yapıdır ve biz herbir objeyi bu yapıya göre üretiriz.
"""

class Araba():
    model = "porsche"
    renk = "cherry blossom"
    beygir_gucu = 350
    silindir = 8
# araba sınıfından nesne ürettik
araba1 = Araba()
araba2 = Araba()
print(araba1.beygir_gucu)
print(araba1.model)
print(dir(araba1))

class Araba():
    model = "porsche"
    renk = "cherry blossom"
    beygir_gucu = 350
    silindir = 8
    def __init__(self):# objeyi oluşturduğumuz zaman o objeyi gösteren bir referans
        print("init fonksiyonu çağrıldı")


class Araba():
    def __init__(self,model,renk,beygir_gücü,silindir):# init constructor görevi görüyor.
        print("init fonksiyonu çağrıldı")
        self.model = model
        self.renk = renk
        self.beygir_gücü = beygir_gücü
        self.silindir = silindir

araba1 = Araba("911 turbo s","kırmızı",450,8)
araba2 = Araba("corolla","gri",200,4)
print(araba1.model)
print(araba2.model)