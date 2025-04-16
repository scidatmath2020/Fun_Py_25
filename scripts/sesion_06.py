# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 17:01:28 2025

@author: Usuario

"""


#%%


###################################################
################ Coleccion Parte 2 ################
###################################################

len('Hola')

len(["HOla",False,None])

len(("HOla",False,None))

len({"clave1":[1,2,3]})

len({"a",(1,2),0,2025,2,2025})

#%%

#### 0123456789ABCDEF...YZabcdef...yz

max('hola')

max('holOa')

max('ho3lOa')

min('hola')

min('holOa')

min('ho3lOa')

max(["a","x","Z"])
min(["a","x","Z"])


max([2,2,1,3,2025,2])
min([2,2,1,3,2025,2])


max(["hola",5])

max(["hola","adios","verdad"])
min(["hola","adios","verdad"])


max(["hola","adios","Verdad"])
min(["hola","adios","Verdad"])  # Verdad, adios, hola


max(["hola","adios","Verdad",False])

persona = {'nombre':'Juan', 'apellido': 'Pérez', 'promedio':7.5}
### La función max aplicada a un diccionario lo que hace es aplicar
### max a las claves. En este caso, las claves son nombre, apellido y promedio

max(persona)

#%%

#### 0123456789ABCDEF...YZabcdef...yz
#### sort: ordenar de menor a mayor 

sorted("hola")
sorted("holOa")
sorted('ho3lOa')

sorted(["a","x","Z"])
sorted(["a","x","Z","Woman"])
sorted('ho3lOa0')

sorted([2,2,1,3,2025,2])

sorted([2,2,1,3,2025,2],reverse=True)
sorted(["a","x","Z","Woman"],reverse=True)

sorted(["a","x","Z","Woman"])[::-1]

sorted(["hola",5])
sorted([(1+2j),(3+5j)])

persona = {'nombre':'Juan', 'apellido': 'Pérez', 'promedio':7.5}
sorted(persona)
sorted(persona,reverse=True)

#%%%

# La función sum se puede aplicar únicamente cuando la colección
# está formada por numéricos o booleanos

# sum("hola") tira error
sum((1, 45, 11, False))
sum((1, 45, 11, False,True))
sum([1, 45, -11])
sum([True,True,False,True])

"hola a to" + "dos" + ". ¿Cómo están?" 
# "hola a to" & "dos" & ". ¿Cómo están?"

# Este me va a tirar error
persona = {'nombre':'Juan', 'apellido': 'Pérez', 'promedio':7.5}
sum(persona)

#%%

###################################################
########## Conversion de tipos basicos ############
###################################################

type("Hola")
type(-125)
type(3.1416)
type((2+3j))
type([1,5,["a","b"]])
type((1,5,["a","b"]))

saludo = "Hola"
type(saludo)


#%%

int("Hola")

conversion_1 = int("-67")
type(conversion_1)
conversion_1

mi_flotante = -3.1416
type(mi_flotante)
conversion_2 = int(mi_flotante)
conversion_2
type(conversion_2)

int(True)
int(False)

int((2+3j))
int(None)

#%%

float("Hola")

texto_flotante = "-3.1416"
conversion_3 = float(texto_flotante)
type(conversion_3)
conversion_3

float(2025)

float(True)
int(True)

float(False)
int(False)

float((2+3j))

#%%

complex(1,2)
complex(2025)

#%%

bool(0)
bool(-98723897432)

bool("Hola")

bool("")
bool("lkajdlfkj lakjdfalkj lkjdf")
bool(" ")

bool([])
bool([837])

bool(())
bool((""))
bool((" "))

#%%

str(True)
str(False)
str([1,23])
str(-3.1416)
str((2+5j))

persona = {'nombre':'Juan', 'apellido': 'Pérez', 'promedio':7.5}
str(persona)

type(persona)





















