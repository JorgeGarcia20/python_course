def generator(*args):
    """Recibe n cantidad de numeros y regresa el numero ademas\nde regresar True o False si el numero es mayor a 5
    """
    for x in args:
        yield x, True if x > 5 else False
    
name = generator.__name__
document = generator.__doc__
print(name , ' : ')
print(document)