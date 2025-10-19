# dosya açma
"""
bir dosyayı açmak için open() fonksiyonunu kullanıyoruz. yapı ise şu şekilde:
open(dosya_adı,dosya_erişme_kipi)
"""
# w dosya kipi (write)
"""
oluşturmak istediğimiz dizinde öyle bir dosya yoksa w kipi dosyayı oluşturur.
eğer öyle bir dosya zaten varsa da silip tekrar oluituruyor(tehlikeli)
"""
file= open("bilgiler.txt","w")
file.write("Ahmet Kıyran")# dosyaya yazmamızı sağlar.
file.close()# bu da açılan dosyayı kapatmaya yarar.

file = open("bilgiler.txt","a")# a yani appende metodu dosyaya ekleme yapmamızı sağlıyor.
file.write("\nosmaniye")
file.close()