class Usuario:

    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password)
        self.email = email
    
    def __generar_password(self, password):
        return password.upper()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, valor):
        self.__password = self.__generar_password(valor)

jorge = Usuario('Jorge', 'jorge0110', 'jorge@outlook.com')
print(jorge.password)
jorge.password = 'Nuevo password'
print(jorge.password)

    
