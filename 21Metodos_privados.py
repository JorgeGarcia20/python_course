class Usuario:

    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password)
        self.email = email
    
    def __generar_password(self, password):
        return password.upper()

    def get_password(self):
        return self.__password

jorge = Usuario('Jorge', 'jorge0110', 'jorge@outlook.com')
print(jorge.username)
print(jorge.get_password())
print(jorge.email)

    
