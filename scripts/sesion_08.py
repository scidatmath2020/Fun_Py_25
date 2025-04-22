# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 16:58:00 2025

@author: Usuario
"""

'a' in 'Hola'
'b' in 'Hola'
'la' not in 'Hola'

x=217000  

0 in x # tira error porque el lado derecho siempre debe ser una colección

x_texto = str(x)
x_texto

0 in x_texto  # como el lado derecho es un string, el izquierdo también debe
# serlo

"0" in x_texto


lista = ["ahora","xyz",2+5+6+7,True,False,["a",3]]

"ahora" in lista
20 in lista
False in lista
2025 in lista


#%%

True or True
False or True

False and True

not True

15 == 3 or False

15 != 3 or False

15 > 3 and 15 <= 20 

True and 0


## recordar que Python siempre resta un 1 al extremo derecho
"hola a todos"[2:7]  # me devuelve desde la posición 2 hasta la 7-1=6

### Una lista con los múltiplos de 2 o de 5 entre 1 y 1000

lista_numeros = []

for x in range(1,1001):
    if x % 2 == 0 or x % 5 == 0:
        lista_numeros.append(x)
        
        
lista_numeros        
    
for x in range(1,1001):
    if x % 2 == 0 and x % 5 == 0:
        lista_numeros.append(x)

[x for x in range(1,1001) if x % 2 == 0 and x % 5 == 0]

lista_texto = ""

for x in range(1,1001):
    if x % 2 == 0 and x % 5 == 0:
        lista_texto += ", " + str(x)
        
        
lista_texto[2:]        
lista_texto[2:].split(", ")

#%%

x = 58760

"es múltiplo de 10" if x % 2 == 0 and x % 5 == 0 else "Fallaste"

texto = "Pepe Pecas pica papas"
texto = "SciData está impartiendo un curso de Power Bi"
"Ganaste" if len(texto) < 10 or "SciData" in texto else "No pudiste ganar"
"Ganaste" if len(texto) < 10 and "SciData" in texto else "No pudiste ganar"

len(texto)


#%%

texto

texto.split("e")
texto.upper()

lista = [1,2,4,20]

lista.append(texto)


(1+2j).real
(1+2j).imag


"Hola".upper().lower()
"Hola".upper().split("L")

#%%

# 12 * 300

eval("12 * 300")

eval("7 > 10")

eval("'hola'.upper()")

"'hola'.upper()"

# Gokú * 3

Gokú = "Gohan"
eval("Gokú * 3")

del Gokú

Gokú

# 'Gokú' * 3
eval("'Gokú' * 3")
eval("Gokú * 3")

# Hola Mundo
eval("Hola Mundo") #eval("'Hola mundo'")

#'Hola mundo'
eval("'Hola mundo'")

#%%

a = 2

print(a)

b = "hola"

print(b)

lista_numeros

print(lista_numeros)

print(2+57-4)

type(print(2+57-4))

type(lista_numeros)

print(lista_numeros).append("hola")

lista_numeros.append("hola")
print(lista_numeros)

print(2+57-4) * 2

print("Hola","Mundo",2+3)

dinero = 50

print("Hoy gané $" + str(dinero),"en mi trabajo")

texto = "Pepe Pecas pica papas SciData"
respuesta = ("buena" if len(texto) < 10 or "SciData" in texto else "mala")

print("Hoy has tenido " + respuesta + " suerte.")

a
print("Tienes " + a + " buenos amigos.")
print("Tienes " + str(a) + " buenos amigos.")


ganancia = []
perdida = []

signo = input("Es ganancia o pérdida? G/N: ")
valor = float(input("Ingresa el valor numérico: "))

ganancia.append(valor) if signo.upper() == "G" else perdida.append(valor)
    
print(ganancia)
print(perdida)


sum(ganancia) - sum(perdida)







