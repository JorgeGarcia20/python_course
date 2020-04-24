class Circulo:

    #_pi = 3.1416 #podemos definir variables que le pertenecen a la clase
    # creacion de un metodo estatico
    @staticmethod
    def pi():
        return 3.1416

    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return self.radio * self.radio * self.pi()

print(Circulo.pi())
circulo_uno = Circulo(4)
print('El area del circulo es: ',circulo_uno.area())
