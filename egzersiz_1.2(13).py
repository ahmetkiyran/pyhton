# hesap makinesi

islem = input("yapmak istediğiniz işlem simgesini giriniz: (+,-,*,/)")

if(islem == "+"):
    a = int(input("ilk sayıyı giriniz: "))
    b = int(input("ikinci sayıyı giriniz: "))
    print("toplama işlemi sonucu: ",a+b)
elif(islem == "-"): 
     a = int(input("ilk sayıyı giriniz: "))
     b = int(input("ikinci sayıyı giriniz: "))
     print("çıkarma işlemi sonucu: ",a-b)
elif(islem == "*"):
      a = int(input("ilk sayıyı giriniz: "))
      b = int(input("ikinci sayıyı giriniz: "))
      print("çarpma işlemi sonucu: ",a*b)
elif(islem=="/"):
      a = int(input("ilk sayıyı giriniz: "))
      b = int(input("ikinci sayıyı giriniz: "))
      print("bölme işlemi sonucu: ",a/b)
else:
     print("hatalı islem türü seçtiniz...")
     
