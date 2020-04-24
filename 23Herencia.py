"""
Funcionamineto de herencia en python
"""
class Animal:
    @property
    def terrestre(self):
        return True

class Felino(Animal):#asi se espesifica la herencia.
    @property
    def garras_retractiles(self):
        return True
    def cazador(self):
        return 'El felino esta cazando'

class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(self.nombre)

class Gato(Felino, Mascota):
    """
    En esta clase ademas de hacer una herencia multiple, tambien implementamos
    la sobrescritura de metodos, esta solo la usaremos si el metodo o funcion
    sobreescrita hace la misma funcion, si no es asi no es necesario.
    """
    def __init__(self, nombre):
        Mascota.__init__(self, nombre)#asi se espesifica una sobrescritura
        self.nombre_gato = nombre

    def gato_cazador(self):
        self.cazador()

    def mostrar_nombre(self):
        Mascota.mostrar_nombre(self)# sobrescritura de metodos
        print('El nombre del gato es: {}'.format(self.nombre))

class Jaguar(Felino):
    pass

gato = Gato('Canelo')
jaguar = Jaguar()

gato.mostrar_nombre()
print(gato.garras_retractiles)
print(jaguar.terrestre)
