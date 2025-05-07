# -*- coding: utf-8 -*-
"""
Created on Tue May  6 17:07:10 2025

@author: Usuario
"""

# Quiero representar un perro

firulais = {
    "nombre": "Firulais",
    "edad": 4,
    "hambre": True,
    "energia": 50
}

firulais["nombre"]
firulais["edad"]
firulais["hambre"]
firulais["energia"]


firulais["hambre"] = False

firulais["hambre"]



#%%

# Creamos la clase Perro
class Perro:
    pass



firulais_aburrido = Perro()


type(firulais_aburrido)


#%%

"palabra".upper()



#%%

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
perro_con_nombre = Perro("Firulais",4)

perro_con_nombre.nombre
perro_con_nombre.edad
perro_con_nombre.hambre


#%%

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def ladrar(self,alto=True):
        if alto == True:
            print(f"{self.nombre} dice: ¡GUAU!")
        else:
            print(f"{self.nombre} dice: ¡guau!")
        
        
perro_con_ladrido = Perro("Firulais",4)

perro_con_ladrido.nombre
perro_con_ladrido.edad

perro_con_ladrido.ladrar(False)

#%%

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.hambre = True
        self.energia = 50
        self.alimentos = {
            "croquetas": 30,
            "pollo": 40,
            "hueso": 10,
            "sobras": 20
        }

mi_perro = Perro("Benito",8)
mi_perro.nombre
mi_perro.edad
mi_perro.hambre
mi_perro.energia
mi_perro.alimentos



#%%

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.hambre = True
        self.energia = 50
        self.alimentos = {
            "croquetas": 30,
            "pollo": 40,
            "hueso": 10,
            "sobras": 20
        }

    def comer(self, alimento):
        if not self.hambre:
            print(f"{self.nombre} no tiene hambre.")
        else:    
            if alimento not in self.alimentos:
                print(f"{self.nombre} no quiere comer {alimento}.")
            else:
                energia_ganada = self.alimentos[alimento]
                print(f"{self.nombre} está comiendo {alimento} (+{energia_ganada} energía).")
                self.energia += energia_ganada
                if self.energia > 100:
                    self.energia = 100
                self.hambre = False
        
        
    def jugar(self):
        if self.energia >= 20:
            print(f"{self.nombre} está jugando.")
            self.energia -= 20
            self.hambre = True
        else:
            print(f"{self.nombre} está muy cansado para jugar.")
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo.")
        self.energia = 100
        self.hambre = True

    def estado(self):
        hambre_str = "sí" if self.hambre else "no"
        print(f"{self.nombre} tiene {self.edad} años.")
        print(f"Energía: {self.energia}")
        print(f"¿Tiene hambre?: {hambre_str}")
        
        
mi_perro = Perro("Benito",5)


mi_perro.estado()

mi_perro.dormir()
        
mi_perro.estado()        

mi_perro.jugar()

mi_perro.estado()        

mi_perro.jugar()

mi_perro.estado()        

mi_perro.jugar()

mi_perro.estado()        

mi_perro.jugar()

mi_perro.estado()        

mi_perro.jugar()

mi_perro.estado()        
        
mi_perro.jugar()        
mi_perro.estado() 


mi_perro.comer("carnitas")
mi_perro.estado() 

mi_perro.comer("pollo") 
mi_perro.estado() 


mi_perro.jugar()  
mi_perro.estado()


mi_perro.comer("croquetas") 
mi_perro.estado()

mi_perro.dormir()
mi_perro.estado()



mi_perro.hambre = False

mi_perro.edad = 10

mi_perro.alimentos["carnitas"] = 5

mi_perro.alimentos

mi_perro.jugar()

mi_perro.estado()

mi_perro.comer("carnitas")

mi_perro.estado()


#%%

class PerroDeServicio(Perro):
    def __init__(self, nombre, edad, persona_asignada):
        super().__init__(nombre, edad)
        self.persona_asignada = persona_asignada

    def asistir(self):
        if self.energia >= 40:
            print(f"{self.nombre} está asistiendo a {self.persona_asignada}.")
            self.energia -= 40
            self.hambre = True
        else:
            print(f"{self.nombre} no tiene suficiente energía para asistir.")
    
    def estado(self):
        super().estado()
        print(f"Persona asignada: {self.persona_asignada}") 


perro_ayudante = PerroDeServicio("Firulais", 5, "José Manuel")

perro_ayudante.estado()


perro_ayudante.hambre
perro_ayudante.comer("carnitas")

perro_ayudante.comer("hueso")

perro_ayudante.estado()


perro_ayudante.asistir()

perro_ayudante.estado()

perro_ayudante.comer("hueso")

perro_ayudante.estado()

perro_ayudante.asistir()

perro_ayudante.jugar()

perro_ayudante.estado()

perro_ayudante.dormir()

perro_ayudante.estado()







