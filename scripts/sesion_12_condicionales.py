# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 16:59:48 2025

@author: Usuario
"""

### if simple


"""Script que ejemplifica el uso del condicional if.
   Si se ingresa un texto igual a "gato", se desplegará el mensaje "miau"."""

# "Weiersetraß".casefold()


animal = input("¿Qué animal es? ")

2+3
valor = "hola"*5
print(valor)

if animal.casefold() == "gato":
    print("miau")
    valor = 2*valor
    
   
print("Sólo los gatos maullan.")

print(valor)

#%%

# if...else

"""Script que ejemplifica el uso de la estructura condicional if-else.
   Si se ingresa un texto igual a "gato", se desplegará el mensaje "miau", 
introducir cualquier otro texto desplegará "no sé que ruido hace ese animal." """

animal = input("¿Qué animal es? ")
print(f"Este animal es un {animal}")
2+3
valor = "Me gusta SciData " * 2
print(valor)


if animal.lower() == "gato":
    print("miau")
    valor = 3*valor
else:
    print("No sé que ruido hace este animal.")
    valor = 5*valor
    
    
    
print(f"Sólo los gatos maullan. Además valor vale:\n{valor}")

#%%

guerrero = input("Nombra un Guerrero\n")
valor = int(input("Indica el nivel de pelea\n"))

if guerrero == "Yamcha" or valor < 1000:
    print("Seguro se va a morir")
else:
    print(f"Tenemos oportunidad de que {guerrero} nos salve")
    
print("Así pasa en DBZ")

#%%

guerrero = input("Nombra un Guerrero\n")  
valor = int(input("Indica el nivel de pelea\n"))

# Gokú con 3000

if guerrero == "Yamcha" or valor < 1000:
    print("Seguro se va a morir")    
else:
    if guerrero == "Gokú":
        print(f"Qué bien! Aunque el poder de Gokú es de {valor}, es capaz de aumentarlo hasta {valor+20000}.")
    else:
        print(f"Muy bien. {guerrero} es muy fuerte, pero Gokú tiene al guión de su lado.")
    print(f"Tenemos oportunidad de que {guerrero} nos salve")
    
print("Así pasa en DBZ")

#%%

"""Script que ejemplifica el uso de la estructura condicional if-elif-else.
Si se ingresa un texto igual a alguno de los nombres de animales, se desplegará
el mensaje correspondiente, introducir cualquier otro texto desplegará 
"no sé que ruido hace ese animal." """


animal = input("¿Qué animal sugiere? ")

print(f"Este animal es {animal}.")

if animal == "gato":
    print("miau")
elif animal == "perro":
    print("guau")
elif animal == "pez":
    print ("glub glub")
elif animal == "gallo":
    print("kikiriki")
elif animal == "vaca":
    print("muuu")
else:
    print("No sé que ruido hace este animal.")
    
    
print("Sólo los gatos maullan.")


#%%

animal = input("¿Qué animal sugiere? ")

print(f"Este animal es {animal}.")

valor = "Hola"


if animal == "gato":
    print("miau")
    valor = valor*3
elif animal == "perro":
    print("guau")
    valor = valor*5
elif animal == "pez":
    print ("glub glub")
elif animal == "gallo":
    print("kikiriki")
elif animal == "vaca":
    print("muuu")
    valor = "Hola a todos"
else:
    print("No sé que ruido hace este animal.")
    
    
print("Sólo los gatos maullan.")

#%%


guerrero = input("Nombra un guerrero\n")

if guerrero == "Yamcha" or guerrero == "Krilin":
    print(f"{guerrero} es un humano")
elif guerrero == "Gokú" or guerrero == "Vegueta":
    print(f"{guerrero} es un saijajin")
elif guerrero == "18" or guerrero == "17":
    print(f"{guerrero} es un androide")
elif guerrero == "Pikoro":
    print(f"{guerrero} es un namekuseí")
else:
    print(f"{guerrero} no es un personaje importante")

print("Esas son razas de DBZ")

#%%

nombres_columnas = ["nombre", "apellido", "calculo1","tipo1", "calculo2", 
                    "indice1", "indice2", "tipo2","indice3", "tipo3"]

delitos_violento = []
delitos_fraude= []
delitos_robo = []

for columna in nombres_columnas:
    if columna.startswith("tipo"):
        print("Columna de delito violento")
        delitos_violento.append(columna)
    elif columna.startswith("indice"):
        print("Columna de tipo fraude/extorsión")
        delitos_fraude.append(columna)
    elif columna.startswith("calculo"):
        print("Columna de tipo robo")
        delitos_robo.append(columna)
    else:
        print("Columna que no mide delitos")
    
    
    
delitos_violento    
delitos_fraude
delitos_robo
    
#%%

# if anidado

"""Script que ejemplifica el uso de condicionales anidados. Validará si un valor 
ingresado sea entero, ademá de validar si es positivo o negativo."""

dato_texto = input('Ingrese un número entero: ')
dato = eval(dato_texto) # entra como "-4" y sale como -4

if type(dato) is int:
    print('Es un entero.')
    if dato < 0:
        print('Es negativo.')
    elif dato > 0:
        print('Es positivo.')
    else:
        print('Es cero')
else:
    print('No es un entero.')

#%%

# Un script que me diga el nombre del día de la semana

dia = int(input("Dime un número entre 1 y 7: "))

if dia == 1:
    print("El dia es lunes.")
else:
    if dia == 2:
        print("El dia es martes")
    else:
        if dia ==3:
            print("El día es miércoles")
        else:
            if dia == 4:
                print("El dia es jueves")
            else:
                if dia == 5:                    
                    print("El dia es viernes")
                else:
                    print("El día es fin de semana")
    

dia = int(input("Dime un número entre 1 y 7: "))
    
if dia == 1:
    print("El dia es lunes")
elif dia == 2:
    print("el dia es martes")
elif dia == 3:
    print("el dia es miercoles")
elif dia == 4:
    print("el dia es jueves")
elif dia == 5:
    print("el dia es viernes")    
else:
    print("Es fin de semana")
    
#%%

dato_texto = input('Ingrese un número entero: ')
dato = eval(dato_texto) # entra como "-4" y sale como -4

if type(dato) is int:
    print('Es un entero.')
    if dato < 0:
        print('Es negativo.')
    elif dato > 0:
        print('Es positivo.')
    else:
        print('Es cero')
else:
    print('No es un entero.')


dato_texto = input('Ingrese un número entero: ')
dato = eval(dato_texto) # entra como "-4" y sale como -4

if type(dato) is int and dato < 0:
    print("es un entero.")
    print("Es negativo")
elif type(dato) is int and dato == 0:
    print("es un entero.")
    print("Es cero")
elif type(dato) is int and dato > 0:
    print("es un entero.")
    print("Es positivo")
else:    
    print('No es un entero.')











