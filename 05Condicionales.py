'''
print('Programa que evalua una calificacion')
calificacion = input('introduce un numero: ')
def resultado(nota):
    valoracion = 'Aprobado'
    if nota<5:
        valoracion = 'Reprobado'
    return valoracion

print(resultado(int(calificacion)))

#PROGRAMA QUE INDICA LA MAYORIA DE EDAD

edad = input('Digita la edad: ')

def comparar(ed):
    if ed < 18 and ed > 0:
        resultado = 'menor de edad'
        return resultado
    elif ed >= 18:
        resultado = 'mayor de edad'
        return resultado
    else:
        return'edad no valida'

comparacion = comparar(int(edad))
print(comparacion)
'''

#CONCATENACION DE OPERADORES DE COMPARACION
sueldo_presidente = int(input('Ingresa el sueldo del presidente: '))
print('El sueldo del presidente es: '+str(sueldo_presidente))

sueldo_director = int(input('Ingresa el sueldo del director: '))
print('El sueldo del director es: '+str(sueldo_director))

sueldo_supervisor = int(input('Ingresa el sueldo del supervisor: '))
print('El sueldo del supervisor es: '+str(sueldo_supervisor))

sueldo_administrador = int(input('Ingresa el sueldo del administrador: '))
print('El sueldo del administrador es: '+str(sueldo_administrador))

if sueldo_administrador < sueldo_supervisor < sueldo_director < sueldo_presidente:
    print('Todo esta en orden')
else:
    print('Algo anda mal')