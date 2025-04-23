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








  