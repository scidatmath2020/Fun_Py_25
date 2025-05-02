# -*- coding: utf-8 -*-
"""
Created on Thu May  1 17:17:16 2025

@author: Usuario
"""

###

mi_conjunto = {1,"hola",("cómo estás?",1,5),[2,6,"hooooola"]}

# {1,2,3,{0}}

mi_lista = ["hooa",1,2025, False]

set(mi_lista)

#%%

set({'id_1': 3, 'id_2': 4, 'id_3': 5, 'id_4': 6})

{[[12, 3, 27], [True, 60]]}

set(   [    [12, 3, 27], [True, 60]    ]   )

#%%

{1,3,1,1,5,7,1,3}
conjunto = {1, 'dos', 3.0, '4'}

conjunto
#%%

#.add

conjunto.add(1.0)
conjunto

conjunto.add("uno")
conjunto

#%%

# remove
conjunto

conjunto.remove("SciData")   # Como no lo encuentra, llora
conjunto.remove("uno")
conjunto

otro = {1,3,1,1,5,7,1,3}
otro.remove(1)
otro.remove(1)

#%%

# .discard

conjunto = {1, 'dos', 3.0, '4'}

conjunto.discard(1)
conjunto

conjunto.discard("SciData")  # No lo encuentra, pero no llora
conjunto

#%%

# .pop

conjunto = {1, 'dos', 3.0, '4'}
conjunto

conjunto.pop()
conjunto

conjunto.pop()
conjunto

#%%

#### unique(c(1,1,4,2,6,7,2)) resulta en c(1,4,2,6,7)
#### set([1,1,4,2,6,7,2]) resulta en [1,4,2,6,7]

conjunto = {1, 'dos', 3.0, '4'}
conjunto.clear()
conjunto

#%%

marinos = {"Popeye", "Bluto", "Brutus", "Capitán", "Alice the Goon"}
civiles_b = {"Olive Oyl", "Swee'Pea", "Wimpy", "Jeep","Bluto"}
civiles = {"Olive Oyl", "Swee'Pea", "Wimpy", "Jeep"}
            

#%%

# isdisjoint: son disjuntos? Es decir ¿NO tienen elementos en común?

marinos.isdisjoint(civiles_b)
marinos.isdisjoint(civiles)

civiles.isdisjoint(marinos)

#%% 

# issubset: A.issubset(B) significa ¿A es un subconjunto de B?

marinos.issubset(civiles_b)
civiles.issubset(civiles_b)

#%%

# issuperset: A.issuperset(B) significa ¿B es un subconjunto de A?
civiles_b.issuperset(marinos)
civiles_b.issuperset(civiles)

#%%

### .union

marinos.union(civiles_b)
civiles_b.union(marinos)

marinos
civiles_b

### .update

marinos.update(civiles_b)
marinos
civiles_b


#%%

marinos = {"Popeye", "Bluto", "Brutus", "Capitán", "Alice the Goon"}
civiles_b = {"Olive Oyl", "Swee'Pea", "Wimpy", "Jeep","Bluto"}
civiles = {"Olive Oyl", "Swee'Pea", "Wimpy", "Jeep"}
            
marinos.difference(civiles_b)

civiles_b.difference(marinos)

#%%


marinos.intersection(civiles_b)
civiles_b.intersection(civiles)

civiles_b.intersection(marinos)

#%%

marinos.symmetric_difference(civiles_b)
civiles_b.symmetric_difference(marinos)

#%%

prueba = {"hola","mate","hace calor",2025,False}

prueba.symmetric_difference(prueba)

#%%

# frozenset

mi_frozen1 = frozenset([1, 'dos', 3.0, '4'])
mi_frozen2 = frozenset(["uno", 'dos', 3.0, '4'])


mi_frozen1.intersection(mi_frozen2)

#%%






























