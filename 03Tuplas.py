'''
TUPLAS
son listas inmutables, es decir, no se puede modificar depsues de su creacion
    no permite añidor, eliminar, mover elemtos etc(no append, extends, remove)
    si permite extraer porciones, pero el resultado de la extraccion no es una tupla nueva
    no permite bbusqyedas(no index)
    si perimite comprobar si un elemnto se encuentra en la tupla

¿que utilidad o ventaja tiene respecto a las listas?
    mas rapidas
    menos espacio(mayor optimizada)
    formatean strings
    puede utilizarse como claves de un diccionario.(las listas no)

'''
miTupla=('jorge', 20, 10 , 1999)#las tuplas se crean con parentesis y no con corchetes
#podemos comvertir una tupla a lista
miLista=list(miTupla)
'''
podemos comvertir una lista en una tupla con la funcion tuple
miLista[1,2,4,5]
mitupla = tuple(miLista)
y esto convierte una lista en una tupla
'''
print(miLista)
print(miTupla)

#para saber si existen elementos en la tupla
print('jorge' in miTupla)

#el metodo count nos dice cuantas veces existe el elemento existen en la tupla
print(miTupla.count(20))

#pasa saber cuantos elementos existen en una tupla se usa len
print(len(miTupla))

#DESENPAQUETADO DE TUPLAS
#asignamos el valor de un elemto a una variable y despues podemos usar esa variable
nombre, dia, mes , agno=miTupla
print(nombre)
print(dia)
print(mes)
print(agno)
