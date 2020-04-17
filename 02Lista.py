'''
listas:
estructura de datos que nos permite almacenar gran cantidad de valores
(equivalente a los arrays en otras leguajes de programacion)
en python las listas pueden guardad diferente tipo de valores(en otros
lenguajes no ocurre esto con un array).
se puede expandir dinamicamente añadiendo nuevos elementos
(otra novedad respecto a los arrays en otros lenguajes).
'''
miLista=['hola', 'mundo', 'como estan', 'yo sad', 'pero da igual', 'y tu?']

#para insertar nuevos elementos a la lista usamos append
miLista.append('hello')

#para insertar un nuevo elemnto en una posicion exacta usamos insert
miLista.insert(2,'ciao')

#para insertar mas de un objeto en la listas usamos extend
miLista.extend([1,2,3])


print(miLista[:])#imprime toda la lista

#para saber el indice de algun elemento usamos index
print(miLista.index('ciao'))

#para saber si un elemnto se encuestra en la lista
print('jorge' in miLista)

#para eliminar algun elemto en la lista usamos remove mas el indice donde esta el elemento
miLista.remove('hello')
print(miLista)

#para eliminar  el ultimo elemento de la lista usamos pop
miLista.pop()
print(miLista)

'''
si queremos sumas dos listas podemos hacer lo siguinete
lista1 = [elementos]
lista2 = [elementos]

lista3 = [lista1 + lista2]
print(lista3) y obtendremos una lista con los elemtos de las dos listas sumandas

'''

#imprime el indice 
#print(miLista[3])

#python puede leer indices negativos
#print(miLista[-2]) 

#podemos crear un rango
#print(miLista[1:4]) 