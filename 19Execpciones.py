"""
try: #inteta hacer 
    print(10/0)
except Exception as ex:#si algi sale mal captura el error
    print(ex) #imprimer el tipo de error 
finally:#apesar de que exista un error esta parte siempre se ejecutara.
    print('Final del programa!')
    
"""
print("-----Ejercio con excepciones-----")
x = float(input("Ingresa in numero: "))
y = float(input("Ingresa otro numero: "))

def division(x, y):
    return x / y

try:
    division(x, y)

except Exception as ex:
    print('______________________________________________')
    print(ex)
    print('algo ha salido mal!')
    print('______________________________________________')

print('Final del programa!')