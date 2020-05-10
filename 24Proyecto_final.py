class TinyIntError(Exception):
    pass

def tiny_int(val):
    return val >=0 and val <= 255
    
try:
    val = 400
    if tiny_int(val):
       print('Numero corecto!')
    else:
        raise TinyIntError('El numero no es correcto, no es un tiny Int :(')

except TinyIntError as error:
    print(error)