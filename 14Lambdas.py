mi_funcion = lambda valor_uno, valor_dos : valor_uno +valor_dos
formato = lambda sentencia : '¿{}?'.format(sentencia)
no_valor = lambda :10
no_resultado = lambda : print('deben ejecutar una accion')

resultado = mi_funcion(3, 7)
print(resultado)

resultado = formato('puedes hacer esto una pregusnta')
print(resultado)

resultado = no_valor()
print(resultado)

resultado = no_resultado()