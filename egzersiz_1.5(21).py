# sayı tahmin oyunu

import random
import time

# 1 ile 40 arasında sayı tahmini

rastgele = random.randint(1,40)
tahmin_hakki = 7
while True:
    tahmin = int(input("tahmininiz: "))

    if(tahmin<rastgele):
        print("bilgiler sorgulanıyor...")
        time.sleep(1)

        print("daha yüksek bir sayı söyleyin...")
        tahmin_hakki -= 1
    elif(tahmin> rastgele):
        print("bilgiler sorgulanıyor...")
        time.sleep(1)

        print("daha düşük bir sayı söyleyin...")
        tahmin_hakki -= 1
    else:
        print("bilgiler sorgulanıyor...")
        time.sleep(1)
        print("tebrikler sayınız",rastgele)
        break
    if(tahmin_hakki == 0):
        print("tahmin hakkınız bitti")
        break