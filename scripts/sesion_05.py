# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 17:15:38 2025

@author: Usuario
"""


"Este es un texto'

"Este es un texto"

'Este es otro texto'



"Y entonces ella me dijo: <<Hola, buena tarde>>."


'Hola Mundo'
"Vamos al McDonald's"
'Kurt Friedrich Gödel'
1+2
"1+2"


str_vacio = ''

#%%

abecedario = ["a","b","c","d","e","f"]

vocales = ["a","e","i"]


mis_vocales = ""

#### indentado
for x in abecedario:
    if x in vocales:
        mis_vocales = mis_vocales + x

mis_vocales

#%%

[1, 2, "tres", True, None]

[None]



abecedario = ["a","b","c","d","e","f"]
vocales = ["a","e","i"]

mis_consonantes = []

for x in abecedario:
    if x not in vocales:
        mis_consonantes.append(x)

mis_consonantes

[False, ['auto', 30, 'gasolina'], 73.12]

#%%

(1, 2, "tres", True, None)

(False, ['auto', 30, 'gasolina'], 73.12)

()

mis_consonantes_tupla = ()

for x in abecedario:
    if x not in vocales:
        mis_consonantes_tupla.append(x)

mis_consonantes_tupla

tupla_none = (None)
tupla_none

lista_none = [None]
lista_none

type(tupla_none)
type(lista_none)


tupla_none_valida = (None,)
tupla_none_valida

type(tupla_none_valida)

#%%

## inmutables: números, textos, tuplas, booleanos
## las claves siempre deben ser inmutables

{'nulo':None, True:'V', 2:[1, 2, 3], '2':False, ('x', 'y'): 15.3}


{"nulo":None,"Booleano":True,"lista":[1,2,3],"Otro_booleano":False}

{"Clave 1":[2,5,1],"Clave 2":[2,5,1]}

{"Clave 1":[2,5,1,3],"Clave 2":None,"Clave 1":[2,5,1]}

{'nombre':'Juan', 'apellido': 'Pérez', [True, 1]:7.5}

#%%

# Un set (conjunto) solo puede contener elementos inmutables

{False, ('auto', 30, 'gasolina'), 73.12}

{3, 2, True, None, 0, False, 3.0, 5, 3., '3', 'Hola', 3, 3, 1}


lista = ["hola","a",3,True,True,3,"hola"]

lista_conjunto = set(lista)

lista_conjunto

len(lista_conjunto)

{False, ['auto', 30, 'gasolina'], 73.12}

{None, {'uno':1, 'dos': 2}}

#%%
"saludo"[0]
'saludo'[10]
'saludo'[-2]

"La migración de las aves es uno de los fenómenos más fascinantes de la naturaleza. Cada año, millones de aves recorren miles de kilómetros entre sus zonas de cría y sus áreas de invernada, guiadas por señales internas y externas que aún no comprendemos del todo. Algunas especies, como el chorlitejo ártico, realizan viajes transcontinentales que desafían los límites de la resistencia animal. Durante el trayecto, enfrentan condiciones climáticas extremas, depredadores y la pérdida de hábitat, lo que convierte su travesía en una proeza digna de asombro. El estudio de estas migraciones no solo nos revela secretos sobre la orientación y la navegación en la naturaleza, sino que también sirve como indicador de la salud de los ecosistemas a nivel global."[15]
"La migración de las aves es uno de los fenómenos más fascinantes de la naturaleza. Cada año, millones de aves recorren miles de kilómetros entre sus zonas de cría y sus áreas de invernada, guiadas por señales internas y externas que aún no comprendemos del todo. Algunas especies, como el chorlitejo ártico, realizan viajes transcontinentales que desafían los límites de la resistencia animal. Durante el trayecto, enfrentan condiciones climáticas extremas, depredadores y la pérdida de hábitat, lo que convierte su travesía en una proeza digna de asombro. El estudio de estas migraciones no solo nos revela secretos sobre la orientación y la navegación en la naturaleza, sino que también sirve como indicador de la salud de los ecosistemas a nivel global."[14]
"La migración de las aves es uno de los fenómenos más fascinantes de la naturaleza. Cada año, millones de aves recorren miles de kilómetros entre sus zonas de cría y sus áreas de invernada, guiadas por señales internas y externas que aún no comprendemos del todo. Algunas especies, como el chorlitejo ártico, realizan viajes transcontinentales que desafían los límites de la resistencia animal. Durante el trayecto, enfrentan condiciones climáticas extremas, depredadores y la pérdida de hábitat, lo que convierte su travesía en una proeza digna de asombro. El estudio de estas migraciones no solo nos revela secretos sobre la orientación y la navegación en la naturaleza, sino que también sirve como indicador de la salud de los ecosistemas a nivel global."[20]

mi_texto = "La migración de las aves es uno de los fenómenos más fascinantes de la naturaleza. Cada año, millones de aves recorren miles de kilómetros entre sus zonas de cría y sus áreas de invernada, guiadas por señales internas y externas que aún no comprendemos del todo. Algunas especies, como el chorlitejo ártico, realizan viajes transcontinentales que desafían los límites de la resistencia animal. Durante el trayecto, enfrentan condiciones climáticas extremas, depredadores y la pérdida de hábitat, lo que convierte su travesía en una proeza digna de asombro. El estudio de estas migraciones no solo nos revela secretos sobre la orientación y la navegación en la naturaleza, sino que también sirve como indicador de la salud de los ecosistemas a nivel global."

mi_texto[15]
mi_texto[14]
mi_texto[20]

lista = [1, 2, 3, 4]
lista[0]
lista[4]
lista[-1]

tupla = (1, [4, True, None, 'Saludo'], 6, 22.5)
tupla[0]
tupla[1]

tupla[1][3][4]

12976323[0]
"12976323"[0]

tupla[-2]

mi_dic = {'nombre':'Juan', 'apellido': 'Pérez', "Calif":7.5}
mi_dic

mi_dic["Otro"]

mi_dic = {'nombre':'Juan', 'apellido': 'Pérez', "Calif":[7.5,8,10]}
mi_dic


mi_dic["Calif"]

#%%

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8]


lista[::-1]

"Saludo"[::-1]

#### Es cierto que "Anita lava la tina" es un palíndromo?

frase = "Anita lava la tina"
invierto = frase[::-1]

invierto

frase == inverto



lista[1:6] # [0, 1, 2, 3, 4, 5, 6, 7, 8]; [1, 2, 3, 4, 5]

frase[3:9]

frase[3:]

frase[ :9]


lista[6:0:-2]


lista[0:6:-2]


lista[5:25]


lista[-2:5]

"Polimorfismo"[ :8:3]

(0,1,2,3,4,5)[:]
(0,1,2,3,4,5)[::-1]

lista

nva_lista = lista[:]

id(lista)
id(nva_lista)

#%%

# mutables: conjuntos, listas, diccionarios
# inmutables: textos, tuplas

mutable = [1, "hola", 3, 4]

del mutable[1]

mutable

mutable[0] = "Número uno"

mutable

inmutable = "12h35"

inmutable[1]

del inmutable[1]

inmutable[1] = "H"

mi_dic

del mi_dic["Calif"]
mi_dic
































































