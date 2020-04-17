def divicion(valor_uno, valor_dos):
    def validacion():
        return valor_uno > 0 and valor_dos >0
    
    if validacion():
        return valor_uno/valor_dos

resultado = divicion(10, 2)
print(resultado)