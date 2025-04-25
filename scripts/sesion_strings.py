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

## casfold()

'HoLA, amiGoS.'.casefold()

# ß = ss

"Weierstraß".lower()

"Weierstrass".lower()

"Weierstraß" == "Weierstrass"

"Weierstraß".lower() == "Weierstrass".lower()

"Weierstrass".casefold()
"Weierstraß".casefold()

"Weierstrass".casefold() == "Weierstraß".casefold()

## center(n,caracter)

len("Hola, amigos.")  # "Hola, amigos.       

"Hola, amigos.".center(15,"x")

"Hola, amigos.".center(21,"x")

"Hola, amigos.".center(14,"-")

# "----Hola, amigos.-----"
"Hola, amigos.".center(22,"-")

# "    Hola, amigos.     "
"Hola, amigos.".center(22)

## ljust(n,caracter)

texto_ljust_30 = 'Hola, amigos.'.ljust(30)
texto_ljust_30
len(texto_ljust_30)


'Hola, amigos.'.ljust(15,"o")

## rjust(n,caracter)

texto_rjust_30 = 'Hola, amigos.'.rjust(30)
texto_rjust_30
len(texto_rjust_30)


'Hola, amigos.'.rjust(18,"A")

## strip(texto)

'                 Hola, amigos.  '.strip()

'Hola, amigos.'.rjust(18,"A").strip("A")


'xxxxxxxxxxxxxxxxxHola, amigos.xxxxxxxx'.strip("x")

## lstrip(texto)

'                 Hola, amigos.        '.lstrip()
'xxxxxxxxxxxxxxxxxHola, amigos.xxxxxxxx'.lstrip("x")

## rstrip(texto)

'                 Hola, amigos.        '.rstrip()
'xxxxxxxxxxxxxxxxxHola, amigos.xxxxxxxx'.rstrip("x")

## expandtabs(n)

'Hola\tamigos'
print('Hola\tamigos')

'Hola\tamigos'.expandtabs()
len('Hola\tamigos'.expandtabs())


'Hola\tamigos'.expandtabs(2)
'Hola\tamigos'.expandtabs(10)

'Hola\tamigos\tde\tSciData'.expandtabs()

## zfill(n) la z es de zero. Rellena con n ceros a la izquierda

'Hola'.zfill(6)

'504'.zfill(7)

## join()


"|--|".join(["Hugo", "Paco", "Luis"])

linea1 = "|".join(["Col1","Col2","Col3"])
linea1

linea2 = (3*"--|")[0:8]
linea2

linea3 = "|".join(["a","b","c"])

linea4 = "|".join(["1","876","hola"])

lista_lineas = []

for i in range(1,5):
    lista_lineas.append(eval("linea"+str(i)))
    
# eval("linea" + str(3))
    
lista_lineas
    
print("\n".join(lista_lineas))

" ".join(["Hugo", "Paco", "Luis"])
", ".join(["Hugo", "Paco", "Luis"])


niños = ["Hugo", "Paco", "Luis", "Alondra", "Paty"]

"Los alumnos " + ", ".join(niños[0:4]) + f" y {niños[4]} son buenos estudiantes"

eval(" + ".join(("1", "2", "3", "4")))


' * '.join({'nombre':'Juan', 'apellido':'Pérez'})

## partition

"Hugo, Paco, Luis".partition(",")

"scidata.math@gmail.com".partition("@")


correo = input("Dime tu correo: ")
validacion = correo.partition("@")[2] in ["gmail.com","hotmail.com"]
print("Dominio válido") if validacion == True else print("Dominio inválido")


## rpartition()
"scidata.math@gmail.com".partition("+")


"Hugo, Paco, Luis".rpartition(", ")
"Hugo, Paco, Luis".rpartition(" + ")

## split

"Hugo Paco, Luis".split(" ")
"Hugo Paco, Luis".split(",")

"scidata.math@gmail.com".split("@")


"scidata.math@gmail@com".split("@")

## splitlines

nombres = "Hugo.\nPaco.\nLuis."

nombres.splitlines()

himno = "Mexicanos al grito de guerra\nel acero aprestad y el bridón"
himno.splitlines()

## find()

'Luis, Hugo, Paco, Luis, Paco'.find('Paco')
'Luis, Hugo, Paco, Luis, Paco'.find('Pedro')

frase = 'Paco, Luis, Hugo, Paco, Luis, Paco, Paco, Hugo, Paco, hola a Paco, adios'

# ¿En qué índices se encuentra la palabra "Paco": [12, 24, 30, 42]

lista_apariciones = []

N = len(frase)

while frase.find("Paco") != -1:
    lista_apariciones.append(frase.find("Paco"))
    frase = frase.partition("Paco")[2]  # , Luis, Paco, Paco, Hugo, Paco
    frase = frase.zfill(N) #    000000000000, Luis, Paco, Paco, Hugo, Paco
    
lista_apariciones    
    
#%%

## index
"Luis, Alberto, Miguel".find("Paco")


"Luis, Alberto, Miguel".index("Miguel")

"Luis, Alberto, Miguel".index("Paco")

'Luis, Hugo, Paco, Luis, Paco, Paco, Hugo, Paco, hola a Paco, adios'.index("Paco")
'Luis, Hugo, Paco, Luis, Paco, Paco, Hugo, Paco, hola a Paco, adios'.index("Héctor")

#%%

### replace

'Luis, Hugo, Paco, Luis'.replace('Luis', 'Juan Antonio')
'Luis, Hugo, Paco, Luis'.replace('Pedro', 'Juan')

#%%

### count()

"Hola, amigos.". count("a")


frase = 'Paco, Luis, Hugo, Paco, Luis, Paco, Paco, Hugo, Paco, hola a Paco, adios'

# ¿En qué índices se encuentra la palabra "Paco": [0, 18, 30, 36, 48, 61]

lista_apariciones = []

N = len(frase)

while frase.count("Paco") != 0:
    lista_apariciones.append(frase.find("Paco"))
    frase = frase.partition("Paco")[2]  # , Luis, Paco, Paco, Hugo, Paco
    frase = frase.zfill(N) #    000000000000, Luis, Paco, Paco, Hugo, Paco
    
lista_apariciones


"Hola, amigos.".count("Héctor")


cancion = "Ay amor mío, qué terriblemente absurdo es estar vivo"
cancion.count("qué terriblemente")


#%%

## startswith


"Hola, amigos.".startswith("la")
"Hola, amigos.".startswith("Hol")


######## nombre, apellido, calculo1, calculo2, indice1, indice2, indice3, tipo1, tipo2, tipo3


nombres_columnas = ["nombre", "apellido", "calculo1","tipo1", "calculo2", 
                    "indice1", "indice2", "tipo2","indice3", "tipo3"]

columnas_delitos_graves = []


for texto in nombres_columnas:
    if texto.startswith("tipo") == True:
        columnas_delitos_graves.append(texto)
        
columnas_delitos_graves


### Encontrar cuántas vocales tiene una frase

vocales = ["a","e","i","o","u","á","é","í","ó","ú"]

frase = "Estoy tomando el cúrso de pythOn desde cero"

mis_vocales = []

for letra in frase:
    if letra.lower() in vocales:
        mis_vocales.append(letra)
        
len(mis_vocales)
set(mis_vocales)

conteos = []

for vocal in vocales:
    conteos.append(frase.count(vocal) + frase.count(vocal.upper()))
    
sum(conteos)

#%%

## endswith()

"Hola, amigos.".endswith("Hola")
"Hola, amigos.".endswith("gos.")

#%%
## isalnum()
## 0123456789 y las letras 

"@#%&".isalnum()


"Héctor14Luis".isalnum()

"Héctor14Lu is".isalnum()

"Héctor+14Luis".isalnum()


intentos = 0

while intentos < 3:
    contraseña = input("Crea tu contraseña. Solo puede tener caracteres alfanuméricos: ")
    if contraseña.isalnum() == False:
        print("Esa contraseña no cumple el requerimento. Intenta de nuevo")
    else:
        print("Contraseña válida")
        break
    intentos += 1
    
#%%

# isalpha()

"@#%&".isalpha()

"Héctor12".isalpha()

"Héctor Manuel".isalpha()

"PepePecasPicaPapas".isalpha()

#%%

# isnumeric()

'0x1a'.isnumeric()

'-22.1'.isnumeric()

'-221'.isnumeric()

'221'.isnumeric()

#%%

# isdecimal()

'0x1a'.isdecimal()

'-22.1'.isdecimal()

'22.1'.isdecimal()

'23'.isdecimal()

'2²'.isdecimal()

'2²'.isnumeric()

'½'.isdecimal()

#%% islower()

'¡hola, amigos!'.islower()

'¡hola, amiGos!'.islower()

### isupper()

'¡HOLA, AMIGOS!'.isupper()
'¡HOLA, AmIGOS!'.isupper()

### istitle()

# "Hola a todos".title()

# "hola a todos".capitalize()

'¡HOLA, AMIGOS!'.istitle()

"Hola, Amigos".istitle()

"¡Hola, Amigos!".istitle()

#%%

# isprintable

lineas = "Hugo.\nPaco.\nLuis."

print(lineas)

lineas.isprintable()

espacios = "Hugo.\tPaco.\tLuis."

print(espacios)

espacios.isprintable()

#%%

# isspace()

'   '.isspace()

''.isspace()

'a bc'.isspace()

'                          '.isspace()

#%%

'Nombre'.isidentifier()

Nombre = "Este es un texto"

"Héctor Manuel".isidentifier()

Héctor Manuel = "Este es un texto"

"ab@c".isidentifier()

ab@c = 1+4+2

#%%

trans = str.maketrans("áäàéëèíïìóöòúüù", "aaaeeeiiiooouuu")


'Hólá amïgòs. ¿Cómö éstán?'.translate(trans)

mi_frase = 'Hólá amïgòs. ¿CómÖ éstán?'

# Cuántas vocales tiene

vocales = ["a","e","i","o","u"]

trans = str.maketrans("áäàéëèíïìóöòúüù", "aaaeeeiiiooouuu")
frase_limpia = mi_frase.lower().translate(trans)

frase_limpia

mis_vocales = []

for letra in frase_limpia:
    if letra.lower() in vocales:
        mis_vocales.append(letra)
        
len(mis_vocales)























        























  