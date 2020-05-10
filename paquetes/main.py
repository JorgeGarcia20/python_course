"""
para crear paquetes en Python es necesario tener un directorio
dentro de ese directorio es necesario crear un fichero llamado
__init__ ademas de los ficheros necesarios.
"""
#Despues de agregar .gato en init el llamar la Clase Gato
from animales import Gato 
from animales import Leon
from animales import nombrar_gato

gato = nombrar_gato('Mi nombre es canelo miau! :3')
print (gato.nombre)