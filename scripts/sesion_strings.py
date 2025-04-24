# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 18:42:44 2025

@author: Usuario
"""

'Hola, mundo'[1]
'Hola, mundo'[-5:-2]
"hola, mundo"[2:8]
"hola, mundo"[::-1]


saludo = "HOla amigos"
saludo[1] = 'a'


## lower()

'Hola, amigos.'.lower()
"LKJjhdHIjklsd".lower()


palabra = input("Dame la clave.\nPista: es un animal:\n")
print("Clave correcta") if palabra.lower() == "gato" else print("Clave incorrecta")

# upper()

'Hola, amigos.'.upper()

palabra = input("Dame la clave.\nPista: es un animal:\n")
print("Clave correcta") if palabra.upper() == "GATO" else print("Clave incorrecta")


## capitalize()  (mayúscula en inglés se dice capital)

'hola, amigos.'.capitalize()

"GATO".capitalize()

palabra = input("Dame la clave.\nPista: es un animal:\n")
print("Clave correcta") if palabra.capitalize() == "Gato" else print("Clave incorrecta")

## title()

'hola, amigos.'.title()
"mi primer tesis".title()


## swapcase()

'Hola, amigos.'.swapcase()

## casfold()

'HoLA, amiGoS.'.casefold()

# ß = ss

"Weierstraß".lower()

"Weierstrass".lower()

"Weierstraß" == "Weierstrass"

"Weierstraß".lower() == "Weierstrass".lower()

"Weierstrass".casefold()
"Weierstraß".casefold()

"Weierstrass".casefold() == "Weierstraß".casefold()

## center(n,caracter)

len("Hola, amigos.")  # "Hola, amigos.       

"Hola, amigos.".center(15,"x")

"Hola, amigos.".center(21,"x")

"Hola, amigos.".center(14,"-")

# "----Hola, amigos.-----"
"Hola, amigos.".center(22,"-")

# "    Hola, amigos.     "
"Hola, amigos.".center(22)

## ljust(n,caracter)

texto_ljust_30 = 'Hola, amigos.'.ljust(30)
texto_ljust_30
len(texto_ljust_30)


'Hola, amigos.'.ljust(15,"o")

## rjust(n,caracter)

texto_rjust_30 = 'Hola, amigos.'.rjust(30)
texto_rjust_30
len(texto_rjust_30)


'Hola, amigos.'.rjust(18,"A")

## strip(texto)

'                 Hola, amigos.  '.strip()

'Hola, amigos.'.rjust(18,"A").strip("A")


'xxxxxxxxxxxxxxxxxHola, amigos.xxxxxxxx'.strip("x")

## lstrip(texto)

'                 Hola, amigos.        '.lstrip()
'xxxxxxxxxxxxxxxxxHola, amigos.xxxxxxxx'.lstrip("x")

## rstrip(texto)

'                 Hola, amigos.        '.rstrip()
'xxxxxxxxxxxxxxxxxHola, amigos.xxxxxxxx'.rstrip("x")

## expandtabs(n)

'Hola\tamigos'
print('Hola\tamigos')

'Hola\tamigos'.expandtabs()
len('Hola\tamigos'.expandtabs())


'Hola\tamigos'.expandtabs(2)
'Hola\tamigos'.expandtabs(10)

'Hola\tamigos\tde\tSciData'.expandtabs()

## zfill(n) la z es de zero. Rellena con n ceros a la izquierda

'Hola'.zfill(6)

'504'.zfill(7)

## join()


"|--|".join(["Hugo", "Paco", "Luis"])

linea1 = "|".join(["Col1","Col2","Col3"])
linea1

linea2 = (3*"--|")[0:8]
linea2

linea3 = "|".join(["a","b","c"])

linea4 = "|".join(["1","876","hola"])

lista_lineas = []

for i in range(1,5):
    lista_lineas.append(eval("linea"+str(i)))
    
# eval("linea" + str(3))
    
lista_lineas
    
print("\n".join(lista_lineas))

" ".join(["Hugo", "Paco", "Luis"])
", ".join(["Hugo", "Paco", "Luis"])


niños = ["Hugo", "Paco", "Luis", "Alondra", "Paty"]

"Los alumnos " + ", ".join(niños[0:4]) + f" y {niños[4]} son buenos estudiantes"

eval(" + ".join(("1", "2", "3", "4")))


' * '.join({'nombre':'Juan', 'apellido':'Pérez'})

## partition

"Hugo, Paco, Luis".partition(",")

"scidata.math@gmail.com".partition("@")


correo = input("Dime tu correo: ")
validacion = correo.partition("@")[2] in ["gmail.com","hotmail.com"]
print("Dominio válido") if validacion == True else print("Dominio inválido")


## rpartition()
"scidata.math@gmail.com".partition("+")


"Hugo, Paco, Luis".rpartition(", ")
"Hugo, Paco, Luis".rpartition(" + ")

## split

"Hugo Paco, Luis".split(" ")
"Hugo Paco, Luis".split(",")

"scidata.math@gmail.com".split("@")


"scidata.math@gmail@com".split("@")

## splitlines

nombres = "Hugo.\nPaco.\nLuis."

nombres.splitlines()

himno = "Mexicanos al grito de guerra\nel acero aprestad y el bridón"
himno.splitlines()

## find()

'Luis, Hugo, Paco, Luis, Paco'.find('Paco')
'Luis, Hugo, Paco, Luis, Paco'.find('Pedro')

lista_apariciones = []

frase = 'Luis, Hugo, Paco, Luis, Paco, Paco, Hugo, Paco'

N = len(frase)

while frase.find("Paco") != -1:
    lugar = frase.find("Paco")
    lista_apariciones.append(lugar)
    frase = frase.partition("Paco")[2].zfill(N) 


lista_apariciones
























  