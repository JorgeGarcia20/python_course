def decorador(is_valid = True):
    def _decorador(func):
        
        def before_action():
            print('Vamos a ejecutar la funcion')

        def after_action():
            print('se ejecuto la funcion')

        def new_funtion(*args, **kwargs):
            if is_valid:
                before_action()

            result = func(*args, **kwargs)

            after_action()
            return result
        return new_funtion
    return _decorador
@decorador()
def sum(x, y):
    return x + y

result = sum(80, 90)
print(result)


