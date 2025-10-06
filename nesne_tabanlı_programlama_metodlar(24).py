import time
class Yazılımcı():
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim =soyisim
        self.numara = numara
        self.maaş = maaş
        self.diller= diller
    def bilgilerigöster(self):
      print("""
    yazılımcı objesinin özellikleri
          
    isim: {}
    soyisim: {}
    numara: {}
    maaş: {}
    diller: {}


""".format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
    def zam_yap(self,zam_miktar):
         
         print("zam yapılıyor")
         time.sleep(1)
         self.maaş += zam_miktar

yazılımcı = Yazılımcı("ahmet","kıyran",2342,840348,"python")

yazılımcı.bilgilerigöster()
yazılımcı.zam_yap(200)
yazılımcı.bilgilerigöster()
