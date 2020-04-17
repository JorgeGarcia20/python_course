"""Ejmemplo del uso del bucle while """
#bucle while controlado por conteo
'''
suma, numero = 0, 1
while numero <= 10:
    suma = numero + suma
    numero = numero+1
print ("la suma es: "+str(suma))

#BUCLE WHILE CONTROLADO POR EVENTO
promedio = 0.0
total = 0
contar = 0

grado = int(input('Introduzca la nota de un estudiante (-1 para salir): '))	
while grado != -1:
    total = total + grado
    contar = contar + 1
    grado = int(input("Introduzca la nota de un estudiante (-1 para salir): "))
promedio = total / contar
print ("Promedio de notas del grado escolar es: " + str(promedio))


#BUCLE WHILE CON ELSE
promedio = 0.0
total = 0
contar = 0

mensaje = 'Introduzca la nota de un estudiante (-1 para salir): '
grado = int(input(mensaje))
while grado != -1:
    total + grado
    contar+1
    grado = int(input(mensaje))
else:
    promedio = total / contar
    print('El promedio total es: ' +str(promedio))
'''
'''
#BUCLE WHILE CONTROLADO POR LA SENTENCIA BREAK
variable = 10
while variable > 0:
    print('el valor actual de la variable es: ', variable)
    variable = variable - 1
    if variable == 5:
        break
'''
'''
adicionalmente existe una forma alternativa de interrumpir o cortar los
ciclos utilizando la palabra reservada break
'''
'''
#BUCLE WHILE CONTROLADO POR LA SENTENCIA CONTINUE
variable = 10
while variable > 0:
    variable = variable-1
    if variable == 5:
        continue
    print('Actual valor de la variable: ', variable)
# La sentencia continue permite que pase de nuevo al bucle aunque no se haya
# terminado de ejecutar el ciclo anterior.
'''
#FUNCION DE FINOBACCI

a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b