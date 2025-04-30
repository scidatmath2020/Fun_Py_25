# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 17:01:03 2025

@author: Usuario
"""

mi_lista = ["a","hola",5,False]
mi_lista


mi_conjunto = {"hola","adiós",0,-3,True}
mi_conjunto

#%%

[ ['automóvil', 50, 'gasolina'], ['autobús', 300]  ]


L1 = [1,2]
L2 = [2,1]

id(L1) == id(L2)

#%%

lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista
lista[1] = "esta es una frase que sustituye al 2 original"

lista[-3] = True

lista

#%%

[[1,2,3],["hola","adiós"],"SciData"][1][1].center(10)

[[1,2,3],["hola","adiós"],"SciData"][1][1].startswith("a")

[[1,2,3],["hola","adiós"],"SciData"][1][1][3]

lista_larga = (["Esta es una primer frase",
               "Esta es una segunda frase",
               "Esta es una tercera frase"])


#%%


lista_larga

# del  es delete
del lista_larga[1]

lista_larga

#%%

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista

del lista[3:8]

lista

#%%

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista[2:6] = ["Este antes era un tres","Este antes era un cuatro",
              "Este antes era un cinco","Este antes era un seis"]

lista

#%%

len(lista)

lista[100] = "Qué puede pasar"


### Tarea: Cómo hago para manipular posiciones que no son continuas
### POr ejemplo, digamos que quiero modificar la posición 2 y la posición 5


#%%

lista_extension = [0,2,4,6,8,10]

lista_compresion = [2*x for x in range(0,6)]

#%%

p1 = "Los guerreros mas poderosos"
p2 = "de todo el universo"
p3 = "aparecen en DBZ"

textos = [p1,p2,p3]

textos_mayusculas = []

for frase in textos:
    textos_mayusculas.append(frase.upper())
    
textos_mayusculas


textos_mayusculas_comprension = [frase.upper() for frase in textos]
textos_mayusculas_comprension

#%%

### POr ejemplo, digamos que quiero mandar a llamar la posición 2 y la posición 5

lista 
posiciones = [2,5,6,9]
[lista[x] for x in posiciones]

  
#%%%

enteros = [229, 902, 627, 869, 795,
366, 804, 237, 5, 979,
778, 939, 990, 499, 177,
252, 446, 571, 348, 734,
367, 162, 731, 492]

[x for x in enteros if x % 5 == 0]

#%%

frases_chat = [
    "Siempre se puede empezar de nuevo.",
    "Sofía salió temprano de casa.",
    "Siente el viento en tu rostro.",
    "Mañana lloverá en la ciudad.",
    "El perro duerme en el sillón.",
    "La luna llena iluminaba el camino.",
    "Hoy cocinaremos pasta al pesto.",
    "La paciencia es una gran virtud.",
    "Todos esperaban el anuncio oficial.",
    "Aprender un idioma abre muchas puertas."
]

["Este es un ejemplo " + frase for frase in frases_chat if frase.startswith("S")]


frases_cortas_comprension = [frase for frase in frases_chat if len(frase) < 30]
frases_cortas_comprension

frases_cortas = []

for frase in frases_chat:
    if len(frase) < 30:
        frases_cortas.append(frase)
        
frases_cortas

#### lapply(frases_chat,function(x){
####                     if(nchar(x) < 30){return(x)}})


#%%

lista_de_listas = [
    [23, 45, 12],
    [88, 91, 4, 36, 55, 29],
    [77],
    [10, 20, 30, 40],
    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
]

lista_de_listas.append("hola")

lista_de_listas

lista_de_listas.append([1,2,3])

lista_de_listas

#%%

# .insert

lista = [1, 2, 3, 4, 5, 6]

lista.insert(3,"hola")
lista   

lista.insert(2,["a","b",True,False])
lista

#%%

# .remove

lista = [1, 2, "hola", 4, 5, 4, "hola", 2, 1, 0,"hola","hola"]
    
lista.remove("hola")

lista

lista.remove(2025)

#%%

### Eliminar todas las palabras "hola" de la lista

lista = [1, 2, "hola", 4, 5, 4, "hola", 2, 1, 0,"hola","hola"]

## 1a forma: por comprensión
[x for x in lista if x != "hola"]

#%%

### Eliminar todas las palabras "hola" y los números 2 de la lista

lista = [1, 2, "hola", 4, 5, 4, "hola", 2, 1, 0,"hola","hola"]

## 1a forma: por comprensión
[x for x in lista if x != "hola" and x != 2]

#%%

### Eliminar todas las palabras "hola"

lista = [1, 2, "hola", 4, 5, 4, "hola", 2, 1, 0,"hola","hola"]

## 2a forma: con for

numero_apariciones = lista.count("hola")

for x in range(0,numero_apariciones):  # x en 0,1,2,3
    lista.remove("hola")
    
lista

#%%
### Eliminar todas las palabras "hola"

lista = [1, 2, "hola", 4, 5, 4, "hola", 2, 1, 0,"hola","hola"]

## 3a forma: con while

while "hola" in lista:  # x en 0,1,2,3
    lista.remove("hola")
    
lista

#%%

# OBSERVACIÓN:
    
## Defino un string
palabra = "SciData"

## Aplico un método
palabra.upper()

## Observo que el objeto original no se modificó
palabra

##########

## Defino una lista
lista = [1, 2, "hola", 4, 5, 4, "hola", 2, 1, 0,"hola","hola"]

## Aplico un método
lista.append("adios")

## Modifica al objeto
lista


#%%

# .reverse()

lista = [1, 2, 3, 4, 5]
lista[::-1]
lista

lista.reverse()

lista

#%%

## .sort

lista = [15, True, 33, False, 12.35,-2]

lista.sort()  # ordena del menor al mayor
lista

###############

lista = [15, True, 33, False, 12.35,-2]

lista.sort(reverse=True) # ordena del mayor al menor
lista


#%%

## .pop()

lista = [15, True, 33, False, 12]


lista.pop(3)

lista

lista.pop(0)

lista


#%%

# .extend


lista_de_listas = [
    [23, 45, 12],
    [88, 91, 4, 36, 55, 29],
    [77],
    [10, 20, 30, 40],
    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
]

lista_de_listas.append([1,2,3])

lista_de_listas


lista_de_listas.extend([1,2,3])
lista_de_listas

graves = ["secuestro","violación","homicidio"]
robos = ["Robo en público","Robo en casa"]
autopartes = ["Robo parcial de vehículo","Robo total de vehículos"]

### Una lista de todos los tipos de delito

graves.append(robos)
graves

########

graves = ["secuestro","violación","homicidio"]
robos = ["Robo en público","Robo en casa"]
autopartes = ["Robo parcial de vehículo","Robo total de vehículos"]

graves.extend(robos)
graves.extend(autopartes)
graves

#%%

#### En .extend(objeto) el objeto debe ser un iterable

lista_ejemplo = [1,2,3,4]

lista_ejemplo.append("hola")
lista_ejemplo

lista_ejemplo = [1,2,3,4]

lista_ejemplo.extend("hola")
lista_ejemplo

#%%

# clear
lista = [93, True, 27, True, True, 16, 45, 14, False, True]

lista.clear()
lista

#%%

## .count()

lista = [1, 2, 3, 4, 5, 4, 3, 2, 1, True, False, True,0,[3,4],[3,4]]
lista.count([3,4])


lista_unicos = [x for x in lista if lista.count(x) == 1]
lista_repetidos = [x for x in lista if lista.count(x) > 1]

#%%

## .index()    
    
lista = [93, True, 27, True, True, 16, 45, 14, False, True]

lista.index(False)
lista.index(18)

lista.index(16)

lista.index(16,3,8)
lista.index(True, 6, 9)



lista

len(lista)

[x for x in range(len(lista)) if lista[x] == True]
















































































#%%

from siuba import *
import pandas as pd
import numpy as np

tabla = pd.DataFrame({"col1":[1,6,2,8,10],
                      "col2":["Aereo","Azul","Beto","Daniel","Alguien"]})



(tabla >>
    filter(_.col2.str.startswith("A")) >>
    select(_.col1))
    

tabla >> filter(_.col2.str.startswith("A")) >> select(_.col1)







    
    
    











