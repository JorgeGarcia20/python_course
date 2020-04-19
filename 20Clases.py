class lapiz:
    """
    este es un ejemplo de clases en python, creacion de clase y definicion de 
    atributos, creacion de objeto e impresion.
    """
    def __init__(self, color, tiene_goma, usa_grafito):
        self.color = color
        self.tiene_goma = tiene_goma
        self.usa_grafito = usa_grafito
    

    #METODOS
    def dibujar(self):
        print('El lapiz esta dibujando')
    
    def borrar(self):
        """
        este metodo recibe el parametro de la funcion puede_borrar
        verifica que la condicion se cumpla y muestra un mensaje.
        ejemplo de usar una funcion dentro de otra funcion.
        """
        if self.puede_borrar():
            print('El lapiz esta borrando')
        else:
            print('El lapiz no tiene borrador')
    
    def puede_borrar(self):
        """
        esta funcion retorna el valor de la variable
        tiene_borrador
        """
        return self.tiene_goma



lapiz_generico = lapiz('Verde', True, True)

print(lapiz_generico.color)
print(lapiz_generico.tiene_goma)
print(lapiz_generico.usa_grafito)

print('---------------Ejecucion de metodos-------------')
lapiz_generico.dibujar()
#lapiz_generico.tiene_borrador = True
lapiz_generico.borrar()

