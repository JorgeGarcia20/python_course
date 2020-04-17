#OPERADORES LOGICOS AND OR Y EL OPERADOR IN
print('Asignatiras del años 2020')
print('Asignaturas: informatica grafica, pruebas de software, ingenieria de software')

asignatura=input('Escribe la asigantura escogida: ')

if asignatura in ('informatica grafica', 'pruebas de software', 'ingenieria de software'):
    print('Asignatura elegida: '+ asignatura)
else:
    print('La asignatura escogida no es contemplada')