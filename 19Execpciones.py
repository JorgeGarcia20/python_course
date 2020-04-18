try: #inteta hacer 
    print(10/0)
except Exception as ex:#si algi sale mal captura el error
    print(ex) #imprimer el tipo de error 
finally:#apesar de que exista un error esta parte siempre se ejecutara.
    print('Final del programa!')