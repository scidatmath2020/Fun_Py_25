# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 17:04:49 2025

@author: Usuario
"""

pi = 3.141592
radio = 3



print("El círculo de radio %s tiene área %s y perímetro %s" 
      %(radio, pi*radio**2,pi*2*radio))

print("El círculo de radio %s tiene área %d y perímetro %d" 
      %(radio, pi*radio**2,pi*2*radio))

print("El círculo de radio %f tiene área %d y perímetro %f" 
      %(radio, pi*radio**2,pi*2*radio))

print("El círculo de radio %e tiene área %e y perímetro %f" 
      %(radio, pi*radio**2,pi*2*radio))


# Quiero el 15% de 13

valor = 13
porciento = 15
porcentaje = (valor * porciento) / 100
print("El %d%% de %f es %f" 
      %(porciento, valor, porcentaje))

#%%

pi = 3.14169265
radio = 2

print("El perímetro de un círculo de radio igual a %d es %.3f" 
      %(radio, 2 * pi * radio))

#%%

curso1 = "Fun_Py"
instructor1 = "Héctor Manuel"
instructor2 = "Cuellar"
edad = 50

# f"........" se trata de un f-string

print(f"Hola. Soy {instructor1}")
print(f"Hola. El resultado de hacer 5*2 es {5*2}")
print(f"Hola. Soy {instructor1 + ' ' + instructor2}")
print(f"Hola. Soy {instructor1 + ' ' + instructor2}. Tengo {edad} años")

pi = 3.14169265
radio = 2

print(f"El perímetro de un círculo de radio igual a {radio} es {2*pi*radio}")


valor = 123.456789

# Mostrar con diferentes cantidades de cifras significativas
print(f"1 cifra significativa: {valor:.1f}")  # a un decimal
print(f"2 cifras significativas: {valor:.2f}")  # a dos decimales
print(f"3 cifras significativas: {valor:.3f}")  # a tres decimales


mi_frase = f"Dos cifras significativas: {valor:.2f}"
mi_frase

print(mi_frase)
mi_frase.upper()

texto = "Pepe Pecas pica papas"
string_personalizado = f"Tienes {'buena' if len(texto) < 10 or 'SciData' in texto else 'mala'} suerte"

string_personalizado

print(string_personalizado)


#%%

"Primera línea.\nSegunda línea\tcon tabulador."
print("Primera línea.\nSegunda línea\tcon tabulador.")


"Esto es una diagonal invertida: \\"
print("Esto es una diagonal invertida: \\")


# ruta = "C:\Users\Usuario\Desktop\escritorio\fun_pbi_2025\AdventureWorks\data"

'Hola\tamigos'

print("Hola\tamigos")
'Hola\tamigos'.expandtabs()


'Gokú fue conocido también por \'Kakarotto\''

print('El signo de \'gato\' es \x23.')

print('I \u2764 YOU!')

'I \u2764 YOU!'

#%%

input("dime tu edad: ")

mi_edad = input("Dime tu edad: ")

mi_edad

type(mi_edad)



texto = input("Dime un texto: ")
string_personalizado = f"Tienes {'buena' if len(texto) < 10 or 'SciData' in texto else 'mala'} suerte"

print(string_personalizado)


calificaciones = []

calificacion = float(input("Dime tu calificación:\n"))
calificaciones.append(calificacion)
calificaciones

promedio = sum(calificaciones) / len(calificaciones)
promedio

CALIFICACIONES = []
total_materias = int(input("¿Cuántas materias vas a ingresar? "))

while len(CALIFICACIONES) < total_materias:
    CALIFICACIONES.append(float(input("Dame la calificación: ")))
    
promedio = sum(CALIFICACIONES)/total_materias

print(f"El promedio es {promedio:.2f}")

#%%

resultado = input("¿Qué operación aritmética quieres que haga?\n")

resultado

# '2+4+8*5-10**3'
mi_salida = eval(resultado)
mi_salida



















print()













