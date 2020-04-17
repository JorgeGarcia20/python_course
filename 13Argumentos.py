def varios_argumentos(*argumentos): # con el * definimos que la funcion podra tener n cantidad de argumentos.
    return argumentos

resultado = varios_argumentos(9,8,3,6,2,4,1)

print(resultado[5])

# con ** definimos que podremos asiganar los argumentos que necesitamos y sus valores.
def argumentos_resultados(**argumentos): 
    
    valor = argumentos.get('string', 'no existe')
    return valor

resultado2 = argumentos_resultados(string = 'jorge', x = 2, z = 7, bol = True)
print(resultado2)

def suma(*numeros):
    
    total = 0
    for valor in numeros:
        total = total + valor
    return total

resultado3 = suma(1,2,3,4,5,6,7,8,9)
print(resultado3)