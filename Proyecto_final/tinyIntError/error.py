class TinyIntError(Exception):
    def __init__(self):
        self.message = 'El numero no cumple con las caracteristicas de un TinyInt.'
    
    def __str__(self):
        return self.message