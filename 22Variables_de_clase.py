class Circulo:

    _pi = 3.1416 #podemos definir variables que le pertenecen a la clase
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return self.radio * self.radio * Circulo._pi

circulo_uno = Circulo(4)
circulo_uno = Circulo(3)

print(Circulo._pi) #Usamos el nombre de la clase mas el nombre de la variable para hacer uso de ella
print(circulo_uno.area())
