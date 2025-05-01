# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 17:11:02 2025

@author: Usuario
"""

####  mi_vector = c(objeto1 = 1,objeto2 = 5, objeto3 = 2, objeto4 = "Hola")

{"nombre": "Juan", "apellido_1": "Pérez", "apellido_2": "Sánchez"}
{1:('Auto', True, 12), "valor":None}
{1.25: 'hola', (12, 23): 'saludo', 12j: True}
{}
codigo_sexo = {1:"Mujer","2":"Hombre"}

#%%

### Con la función dict(), los nombres de las claves no llevan
### comillas

dict(nombre = "Armando", escolaridad_máxima = "Licenciatura")
{"nombre":"Armando","escolaridad_máxima":"licenciatura"}

dict('nombre'= "Armando", 'escolaridad_máxima'= "Licenciatura")

#%%

''' Un par mapeable es una colección de dos elementos, 
en la que el primer elemento es un objeto inmutable y 
el segundo puede ser cualquier objeto'''


mis_pares_mapeables = [ ['nombre', 'Juan'], 
                    ['promedio', 10],
                    ["Estatura",1.75],
                    [2025,("Mate","Inglés","Física")]
                  ]

for sublista in mis_pares_mapeables:
    print(type(sublista[0]))

# Por lo tanto, el primer elemento de cada sublista es inmutable

mi_diccionario = dict(mis_pares_mapeables)
mi_diccionario

#%%

mi_diccionario["nombre"]
mi_diccionario["Estatura"]
mi_diccionario[2025]

mi_diccionario[0]
mi_diccionario["apellido"]

#%%

mi_diccionario
mi_diccionario["nombre"] = "Juan Manuel"
mi_diccionario

mi_diccionario["apellido"] = "Torres"
mi_diccionario

### 

lista = [1,5,2]
lista[4] = 2025

#%%
mi_diccionario

del mi_diccionario["apellido"]

mi_diccionario

#%%

otro_dic = {"nombres":["Alberto","Ariel"],
            "apellido":"Santana",
            "nombres":"Luis"}
otro_dic

otro_dic_dos = {"nombres":["Alberto","Ariel"],
                "apellido":"Santana",
                "padre":"Santana"}

otro_dic_dos

#%%
mi_diccionario = dict(mis_pares_mapeables)
mi_diccionario

#%%
# .pop

mi_diccionario.pop("Estatura")
mi_diccionario

mi_diccionario.pop("canción")

#%%
mi_diccionario
mi_diccionario.popitem()
mi_diccionario


#%%

diccionario_especial = {"a1":"Hola a todos","a2":[1,5,2,5]}

def funcion_eliminadora(ver):
    if ver == True:
        return diccionario_especial.popitem()
    else:
        return list(diccionario_especial.popitem())
    
diccionario_especial

funcion_eliminadora(ver=True)

#%%

mi_diccionario = dict(mis_pares_mapeables)
mi_diccionario

mi_diccionario.get(2025) # como 2025 es una clave, me da su valor
mi_diccionario[2025]  # como 2025 es una clave, me da su valor

mi_diccionario["saludo"] # como "saludo" NO es una clave, me da error
mi_diccionario.get("saludo") # como "saludo" NO es una clave, no devuelve nada

mi_diccionario.get("saludo","No encontré esa clave")

#%%

# update (actualizar)

mi_diccionario.update({"apellido":"González","Actividades":["TKD","FBL"]})
mi_diccionario

mi_diccionario.update([(456,"hola"),("Sexo","Masculino")])
mi_diccionario

#%%

# setdefault
mi_diccionario
mi_diccionario.setdefault("nombre","luis")
mi_diccionario

mi_diccionario.setdefault("correo","blablabla@gmail.com")
mi_diccionario

#%%

# fromkeys

dict.fromkeys(["cv1","cv2","cv3"],(4,1))

#%%

# .clear

mi_diccionario
mi_diccionario.clear()
mi_diccionario


#%%

# .items()

mi_diccionario = dict(mis_pares_mapeables)
mi_diccionario

mi_diccionario.items()
mi_diccionario


# .keys()

mi_diccionario.keys()

# .values()

mi_diccionario.values()

#%%

# Iteraciones

for letra in "HOla a todos":
    print(letra.upper())
    
for palabra in ["hola","a","todos"]:
    print(palabra.upper())
    
for palabra in ("hola","a","todos"):
    print(palabra.upper())
    
mi_diccionario    

for elemento in mi_diccionario:
    if type(elemento) == str:
        print(elemento.upper())
    elif type(elemento) == int:
        print(2*elemento)
    
for elemento in mi_diccionario:
    if type(elemento) == str:
        print(3*mi_diccionario[elemento])
    elif type(elemento) == int:
        print(2*elemento)    

#%%

# enumerate()

iterador = enumerate(("Hugo", "Paco", "Luis"))
type(iterador)

print(iterador)

for x in iterador:
    print(x)

#%%

enumerate("hola")  # (0,"h"),(1,"o"),(2,"l"),(3,"a")

dict(enumerate("hola"))

#%%

enumerate(["Luis","Suárez",32,True,(5,2)])
## (0,"Luis"),(1,"Suárez"),(2,32),(3,True),(4,(5,2))

## La colección anterior se puede convertir en diccionario, porque es una
## colección de pares mapeables

diccionario_sintect = dict(enumerate(["Luis","Suárez",32,True,(5,2)]))
diccionario_sintect 


mis_claves = ["clv1","clv2","clv3","clv4","clv5"]
mis_valores = list(diccionario_sintect.values())

dict([(mis_claves[x],mis_valores[x]) for x in range(5)])




































