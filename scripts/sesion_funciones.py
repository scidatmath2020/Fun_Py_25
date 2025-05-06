# -*- coding: utf-8 -*-
"""
Created on Mon May  5 17:11:56 2025

@author: Usuario
"""

len("este es un texto")
print("Hola a todos")

#####
#%%

# Un algoritmo para contar el total de caracteres de un string

contador = 0

for caracter in "esta es una frase":
    contador = contador + 1
    
contador

#%%

contador = 0

for caracter in "esta es otra frase":
    contador = contador + 1
    
contador

#%%

contador = 0

for caracter in "esta es una tercera frase":
    contador = contador + 1
    
contador

#%%

'''Las funciones me sirven para no tener que estar reescribiendo tanto código'''


def contar_caracteres(texto):
    contador = 0
    for caracter in texto:
        contador = contador + 1
    return contador
        
contar_caracteres("Esta es una frase")
contar_caracteres("Esta es otra frase")
contar_caracteres("Esta es una tercera frase")

'''Una función es una "máquina" que come objetos y devuelve resultados'''

#%%

def funcion_minima():
    pass

funcion_minima()

#%%

def saludo():
    print('Hola')
    
saludo()

#%%

len("mi texto")
?len
?print
?dict

help(len)


saludo()
?saludo

def saludo_documentado():
    '''Esta es una función que imprime la frase "Hola a todos".
    No es una función muy útil '''
    '''Este comentario no aparacerá dentro de la documentación'''
    print("Hola a todos")
    
saludo_documentado()
?saludo_documentado

help(saludo_documentado)

#%%

#variable = "Hola"

def imprimir():
    # ámbito local
    #variable = 2
    print(variable)
    
imprimir()

#%%


## una función que me diga cuántas palabras tiene un texto

def contar_palabras(texto):
    resultado = texto.count(" ")
    return resultado + 1

contar_palabras("Hola a todos. ¿Cómo están?")

mi_texto = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor."
contar_palabras(mi_texto)

# Cuántas vocales tiene el primer párrafo del Quijote

def vocales_Quijote():
    mi_texto = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor."
    mi_texto = mi_texto.lower()
    vocales = ["a","e","i","o","u","á","é","í","ó","ú"]
    total_vocales = 0
    for x in vocales:
        total_vocales = total_vocales + mi_texto.count(x)
    return total_vocales

vocales_Quijote()

#%%

def suma(primero, segundo):
    '''Despliega la suma de exactamente dos objetos'''
    print(primero + segundo)
    
suma(1,5)
suma(2025,7)

suma(1)

#%%

def suma_default(primero,segundo=10):
    print(primero + segundo)
    
    
suma_default(1,7)
suma_default(7,16)
suma_default(2025)  


#%%

# Una función que te permita decidir entre una suma y una resta

def calcular(numero1,numero2,suma=True):
    if suma==True:
        print(numero1 + numero2)
    else:
        print(numero1 - numero2)
        
calcular(5,2)
calcular(5,2,False)
calcular(5,2,True)
 
#%%

def suma_default_error(primero=10,segundo):
    print(primero + segundo)

def calcular(numero1=10,numero2,suma=True):
    if suma==True:
        print(numero1 + numero2)
    else:
        print(numero1 - numero2)
        
        
#%%%

# Una función que calcule el promedio de varios números

def promedio(x,y,z,w):
    print((x+y+z+w)/4)

def promedio(*muestras):
    promedio = sum(muestras)/len(muestras)
    print(f'El promedio de la muestra de {len(muestras)} elementos es {promedio}.')
    
promedio(1,2,3,1,5,2025,-3)


def mi_promedio(lista):
    promedio = sum(lista)/len(lista)
    print(promedio)
    
    
mi_promedio([1,2,56,2,8])    

#%%

def promedio_expon(base,lista):
    promedio = sum(lista) / len(lista)
    print(base**promedio)
    
promedio_expon(2,[6,2,1])

def promedio_expon(base,*lista):
    promedio = sum(lista) / len(lista)
    print(base**promedio)

promedio_expon(2,6,2,1)

def promedio_expon(*lista,base):
    promedio = sum(lista) / len(lista)
    print(base**promedio)
    
promedio_expon(6,2,1,2)

#%%

def superficie(**dato):
    '''Calcula la superficie de una figura geométrica si los parámetros  ingresados
       coinciden.'''
    print(dato)
    if dato["tipo"] == "Rectángulo":
        superficie = float(dato["base"]) * float(dato["altura"])
    elif dato["tipo"] == "Triángulo":
        superficie = float(dato["base"]) * float(dato["altura"]) / 2
    elif dato["tipo"] == "Círculo":
        superficie = float(dato["radio"]) ** 2 * 3.14259265
    else:
        print("No puedo calcular la superficie.")
        superficie = "indefinido"
    print(f"La superficie del {dato['tipo'].lower()} es de {superficie}")
    
superficie(tipo="Triángulo",base=5,altura=2)

superficie(tipo="Triángulo",mediana=5,altura=2)

#%%

def imprimir_saludo(nombre):
    print(f"Hola {nombre}")
    
imprimir_saludo("Héctor")
imprimir_saludo("Luisa")

type(imprimir_saludo("Luisa"))

type(print("Hola"))

f"{imprimir_saludo('Luisa')}. ¿Cómo estás?"


promedio_expon(2,[1,2,6]) + 3

def imprimir_saludo(nombre):
    return f"Hola {nombre}"

type(imprimir_saludo("Héctor"))

imprimir_saludo("Héctor").split()
imprimir_saludo("Héctor").upper()
f"{imprimir_saludo('Héctor')}. ¿Cómo estás?"        



saludo_hector = imprimir_saludo("Héctor")
saludo_luisa = imprimir_saludo("Luisa")

saludo_hector
saludo_luisa

amigos = ["Héctor","Luisa","luis","Ricardo","Raúl","Gloria"]
[imprimir_saludo(x) + ". ¿Cómo estás?" for x in amigos]

def saludo_completo(nombre,sexo,edad,estatura):
    saludo = f"Hola {nombre}."
    if sexo == "masculino":
        sufijo = "o"
        estatura_dif = estatura - 1.70
    else:
        sufijo = "a"
        estatura_dif = estatura - 1.58
    complemento = f"Estimad{sufijo}. Un gusto saludarte"
    edad_2030 = edad + 5
    return (saludo,complemento,edad_2030,round(estatura_dif,2),edad+estatura)

saludo_completo("Luisa","femenino",39,1.70)

#%%

# Una función que cuente cuántas letras a tiene la segunda palabra de una frase

def funcion_anidada(frase):
    auxiliar = frase.lower()
    def contar_a(palabra):
        return palabra.count("a") + palabra.count("á")
    lista_palabras = auxiliar.split(" ")
    palabra_interés = lista_palabras[1]
    letras_a = contar_a(palabra_interés)
    return letras_a

funcion_anidada("En un lugar de la Mancha")
funcion_anidada("Estamos ahora en clase")


#%%

#### 3!=6, 4!=24, 5!=120=4!*5, n! = 1*2*3*...*n, 0!=1

#### Notemos que si n >= 1, entonces n!=(n-1)!*n; 0!=1


def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)
        
factorial(3)
3*factorial(2)
3*2*factorial(1)
3*2*1*factorial(0)
3*2*1*1

factorial(3)

#### Si a es diferente de 0, entonces a^0=1 y a^(n+1)=a^n*a

#### Cálculo de determinantes de una matriz


#%%

# funciones lambda


def imprimir_saludo(nombre):
    return f"Hola {nombre}"


imprimir_lambda = lambda nombre,apellido : f"Hola {nombre} de la familia {apellido}"
imprimir_lambda("Héctor","Garduño")


crear_sufijo = lambda nombre, sexo: f"Estimado {nombre}" if sexo == "masculino" else f"Estimada {nombre}"

crear_sufijo("Luisa","femenino")
crear_sufijo("Héctor","masculino")


























