'''
Diccionarios.
estructura de datos que nos permite almacenar valores de diferente
tipo enterios, cadenas de texto, decimales e incluso listas y otras
diccionarios
laprincipal caracteristica de los diccionarios es qye los datos
se alamacenan asociados a una clave de tal forma que se crea una 
asociasion de tipo calve:valor para cada elemneto almacenado.

los elementos alamacenados no estan ordenados. el orden es
indiferente a la hora de almacenar informacion en un diccionario.


#los diccionarios se crean con llaves
midiccionario={'Alemannia':'Berlin', 'Francia':'Paris','Reino unido':'Londres', 'Mexico':'Toluca'}
#agregar elementos
midiccionario['Italia']='Lisboa'
print(midiccionario)

#modificar valor
midiccionario['Italia']='Roma'
print(midiccionario)

#elimimar elemntos
del midiccionario['Reino unido']
print(midiccionario)
'''
#podemos crear una tupla y asignarle un valor en un diccionario
mitupla=('nombre','carrera','edad','nacionalidad')
diccionario={mitupla[0]:'jorge', mitupla[1]:'ing.sistemas', mitupla[2]:20, mitupla[3]:'mexicana'}
print(diccionario['nombre'])

#una llave dentro de un diccionario puede tener como valor una tupla
diccionario2={'nombre':'jorge', 'edad':20, 'cancionesFavoritas':['suit & tie', 'all apologies', 'hope', 'hablando lento']}
print(diccionario2['cancionesFavoritas']) 
print(diccionario2)

#funciones
#muestras las lleves solamente
print(diccionario.keys)

#muestra los valores solamente
print(diccionario2.values)

#muestra la longitud del diccionario
print(len(diccionario2))


