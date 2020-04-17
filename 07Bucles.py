#BUCLE FOR
'''
for i in [1,2,3,4]:
    print('Hola bb')

#RECORRER STRINGS
for i in['hey', 'you', 3]:
    print('hola', end=' ')

# creamos una variable booleana, evaluamos un correo electronico, si el correo tiene
# @ la variable sera True e imprimira que el correo es correcto
email = input('Introduce tu correo electronico: ')
variable = False
for i in email:
    if i == '@' and '.' :
        variable = True

if variable == True:
    print('El correo es correcto')
else:
    print('El correo es incorrecto')

'''
#TIPO RANGE

for i in range(5):
    print(str(i+1) +'. hola')

#NOTACIONES ESPECIALES CON PRINT