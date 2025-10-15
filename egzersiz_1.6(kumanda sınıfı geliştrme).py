import random
import time

class Kumanda():
    def __init__(self,tv_durumu = "kapalı",tv_ses = 0,kanal_listesi = ["trt"],kanal = "trt"):

        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.kanal_listesi =kanal_listesi
        self.kanal =kanal

    def tv_ac(self):
        if self.tv_durumu == "Açık":
            print("televizyon zaten açık")
        else:
            print("televizyon açılıyor...")
            self.tv_durumu = "Açık"
    def tv_kapat(self):
        if self.tv_durumu == "Kapalı":
            print("televizyon zaten kapalı")
        else:
            print("televizyon kapatılıyor...")
            self.tv_durumu = "Kapalı"

    def ses_ayarları(self):
        while True:
            cevap = input("sesi azalt: sesi azaltmak için '<' artırmak için '>' çıkış için çıkış yaz... ")

            if cevap == "<" :
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print("ses: ",self.tv_ses)
            elif cevap == ">" :
                if self.tv_ses != 31:
                    self.tv_ses += 1
                    print("ses: ",self.tv_ses)
            else:
                print("ses güncellendi: ",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi.")

    def rastgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]

        print("şu anki kanal: ",self.kanal)
        
    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        return "tv durumu:  {}\nTV ses: \nŞu anki kanal: {}\n".format(self.tv_durumu,self.tv_ses,self.kanal_listesi,self.kanal)
    
kumanda = Kumanda()
print("""
Televizyon uygulaması
      
      1. Tv aç
      2. Tv kapat
      3. Ses ayarları
      4. Kanal ekle
      5. Kanal sayısını öğren
      6. Rastgele kanala geçme
      7. Televizyon bilgileri

      çıkmak için q ya basın
""")

while True:

    işlem = input("işlemi seçiniz: ")

    if işlem == "q":
        print("program sonlandırılıyor...")
        break
    elif işlem == "1":
        kumanda.tv_ac()
    elif işlem == "2":
        kumanda.tv_kapat()
    elif işlem == "3":
        kumanda.ses_ayarları()
    elif işlem == "4":
        





