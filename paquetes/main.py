"""
para crear paquetes en Python es necesario tener un directorio
dentro de ese directorio es necesario crear un fichero llamado
__init__ ademas de los ficheros necesarios.
"""
from animales.gato import Gato
gato = Gato('Mi nombre es canelo miau! :3')
print(gato.nombre)