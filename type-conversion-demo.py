
"""

Daire Alanı : pi * r *r 
Daire Çevresi : 2 * pi * r

* yarıçapı verilen bir dairenin alan ve çevresini hesaplayınız.
pi = 3.14

"""

pi = 3.14

yariCap = float(input("yarıçap: ")) 
alan = pi * (yariCap ** 2)

cevre = 2 * pi * yariCap
print("alan",alan)
print("çevre",cevre)