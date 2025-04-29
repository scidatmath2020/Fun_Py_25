# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 17:05:42 2025

@author: Usuario
"""

### while se utiliza cuando no sé cuántas veces se debe realiza una acción



''' Este programa se repetirá 3 veces o hasta que se ingrese
    la palabra "despedida" y desplegará el número de intentos
    hasta que cualquiera de los eventos ocurra.'''

entrada = input("Dame la palabra mágica: ")  #hola
contador = 0

while contador < 3 and entrada != "despedida": #3a iteración: contador=2 y entrada=Héctor
    entrada = input("Entrada fallida. Vuelve a intentarlo: ")  # entrada = SciData
    contador = contador + 1  #contador vale 3
    print(f"Intento número {contador}. \n ")
    
print(f"Utilizaste {contador+1} intentos.")

#%%

''' Este programa se repetirá 3 veces y desplegará el número de intentos en los
    que se ingresó la palabra "despedida".'''

entrada = ""
contador = 1  # cuántos intentos llevo
fallido = 0   # cuántas veces he fallado

#bool(871263)
#bool(0)

while entrada != "despedida":  #recuerda que los numéricos se convierten en True siempre que no sean 0
    entrada = input("Dame la clave: ")
    contador += 1
    # Al ingresar "despedida", se evita que la variable fallido se incremente.
    if entrada == "despedida":
        print("Bien hecho")
        continue 
    print(2+5)
    print("Hola a todos cómo están")
    print(f"Error. Intento {contador-1}\n\n")
    fallido += 1
    
print(f"Tuviste {fallido} intentos fallidos.")


#%%

''' Este programa se repetirá 3 veces o hasta que se ingrese
    la palabra "despedida" y desplegará sólo el número de intentos
    fallidos hasta que cualquiera de los eventos ocurra.'''

contador = 0

while contador < 3:
    entrada = input("Clave: ")
    #Si se ingresa la palabra "despedida, se termina el ciclo.
    if entrada == "despedida":
        break
    contador = contador + 1    
    print(f"Intento {contador}. \n ")

print(f"Tuviste {contador} intentos fallidos.")

#%%

contador = 0

while True:
   print(f"{contador}") 
   if contador == 2025:
      break
   contador = contador + 1
   
contador

#%%

frase = "Hola Pepe, ¿cómo te va?"

exit()


#%%

''' Este programa se repetirá 3 veces o hasta que se ingrese
    la palabra "despedida" y desplegará sólo el número de intentos
    fallidos hasta que cualquiera de los eventos ocurra. Al
    ingresar la palabra "termina" el programa se detendrá.'''

frase = "Hola Pepe, ¿cómo te va?"
operaciones = (3 + 386 * 2)/17634

entrada = ""
contador = 0
while contador < 3:
    entrada = input("Clave: ")
    if entrada == "despedida":
        break
    elif entrada == "termina":
        exit()
    contador = contador + 1
    print(f"Intento {contador} \n ")
    
print(f"Tuviste {contador} intentos fallidos.")



exit()

#%%


for letra in "Chapultepec":
    print(letra.upper())
    
## range()

for x in range(4.3,101,10):  #desde el 5 hasta el 100 de 10 en 10
    print(x)

list(range(5,101,10))

palabra = "Hola a todos"
len(palabra)


for posicion in range(0,len(palabra)+1):
    print(palabra[0:posicion])

#%%

frases_mayúsculas = []

for item in ['uno no es ninguno', 'dos son multitud', 'tres ya son muchos']:
    frases_mayúsculas.append(item.upper())

frases_mayúsculas

###########################################################

frases_mayúsculas = []

for item in ['uno no es ninguno', 'dos son multitud', 'tres ya son muchos',4]:
    if type(item) == str:
        frases_mayúsculas.append(item.upper())
    else:
        frases_mayúsculas.append(item)

frases_mayúsculas

item


###########################################################

frases = ['uno no es ninguno', 'dos son multitud', 'tres ya son muchos',4]
frases_mayúsculas = []

for n in range(0,len(frases)):
    if type(frases[n]) == str:
        frases_mayúsculas.append(frases[n].upper())
    else:
        frases_mayúsculas.append(frases[n])

frases_mayúsculas

n

#%%


list(range(8))

""" Cuenta del 0 hasta 7 en incrementos de a 1."""
for contador in range(8):
    print(contador)
    
""" Cuenta del 5 hasta antes de 9 en incrementos de a 1. """
for contador in range(5, 9):
    print(contador)
    
for contador in range(3, 11, 2):
    print(contador)
    
for contador in range(26, 10, -4):
    print(contador)
    
#%%

num1, num2, texto1, bool1 = 89, 56, "hola", False

## desempaquetado
num1, num2, texto1, bool1 = [89, 56, "hola", False]

for x in [89, 56, "hola", False]:
    if x == 89:
        num1 = x
    elif x == 56:
        num2 = x
    elif x == "hola":
        texto1 = x
    elif x == False:
        bool1 = x

#%%

palabras = ["gato", "pato", "zeta","hola",["Gokú","Vegueta","Trunks","Gohan"]]

for item in  palabras:
    print(item)

for primera, segunda, tercera, cuarta in palabras:
    print(primera)
    print(segunda)
    print(tercera)
    print(cuarta)
    print("-------")

### for siempre se utiliza cuando sé cuántas veces debo realizar una acción





    
    
"Chapultepec"[0:1]




























