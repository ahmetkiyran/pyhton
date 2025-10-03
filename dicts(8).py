
sözlük = {"bir" : 1, "iki" : 2,"üç":3,"dört":4}
print(type(sözlük))
print(sözlük)
print(sözlük["bir"])
sözlük["bir"] = 12 # sözlüğün karşılığını değiştirebiliyoruz
print(sözlük)
print(sözlük.keys()) # sözlükteki anahtar kelimeleri alıyoruz sadece
print(sözlük.values())# sözlükteki değerleri alıyor sadece
print(sözlük.items()) # kendi içinde bir tuples oluşturmaya yarar.