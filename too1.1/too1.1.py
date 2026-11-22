#1

print("Tere, maailm!")


nimi=input("Mis on sinu nimi?")
vanus=input("Mis on sinu vanus?")
print(f"Tere, maailma! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")



#2

vanus=18
eesnimi="Jaak"
pikkus=16.5
kas_käib_koolis=True



# #3

from random import *

kommid_laual = randint(1, 50)
print(f"Laual on {kommid_laual}kommi:")

votta = int(input("Mitu kommi soovid laualt ära võtta? "))

kommid_laual = kommid_laual - votta
print(f"Nüüd on laual {kommid_laual} kommi:")



# #4

import math
umbermoot = float(input("Puu umbermoot (cm):"))
labimoot =  umbermoot / math.pi
print("Puu läbimööt on", round(labimoot, 2), "cm")



#5
import math
n = float(input("N (m): "))
m = float(input("M (m): "))
diagonaal = math.sqrt(n ** 2 + m ** 2)
print("Diagonaal on", round(diagonaal, 2), "m")



# #6

aeg = float(input("Mitu tundi kulus sõiduks?"))
teepikkus = float(input("Mitu kilomeetrit sõitsid?"))
kiirus = teepikkus/aeg
print("Sinu kiirus oli" + str(kiirus)+ "km/h")

#7

a = int(input("Sisesta 1. arv: "))
b = int(input("Sisesta 2. arv: "))
c = int(input("Sisesta 3. arv: "))
d = int(input("Sisesta 4. arv: "))
e = int(input("Sisesta 5. arv: "))
summa = a + b + c + d + e
print("Summa:", summa)
print("Aritmeetiline keskmine:", summa / 5)
jagaja = int(input("Millega summa jagada? "))
print("Täisarvuline osa:", summa // jagaja)
print("Jääk:", summa % jagaja)

#8

print(r'''   @..@
   (----)
  ( \__/ )
^^ "" ^^''')

#9

a=3
b=4
c=5

p=a+b+c
print("Kolmnurga ümbermõõt on", p)




#10

inimesi = int(input("Mitu inimest? "))
hind = 12.90
kokku = hind * 1.10
print("Igaüks maksab", round(kokku / inimesi, 2), "€")