"""
lista = []
for valor in range(0, 101):
    lista.append(valor)
print(lista)
"""

#1- valor a agregar
#2- un ciclo

#podemos agregar las condicionales que deseemos pero entre mas legible sera mejor.
lista = [valor for valor in range(0, 101) if valor % 2 == 0]

tupla = tuple( (valor for valor in range(0, 101) if valor % 2 != 0 ) )

diccionario = {indice:valor for indice, valor in enumerate(lista)}


print(lista)
print('------------------------------------------------------------------')
print(tupla)
print('------------------------------------------------------------------')
print(diccionario)
print('------------------------------------------------------------------')