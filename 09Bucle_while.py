contador = 0
while contador <= 10:
    print(contador)
    contador +=1 # aumentara en uno el contador

    if contador == 5:
        print('estamos en el numero 5')
        continue
    if contador == 6:
        break
else:
    print('El ciclo while ha terminado')


numeros = [1,4,2,5,5,2]
for i in numeros[:]:
    print('hola bb')
