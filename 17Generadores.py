def generator(*args):
    for x in args: #x = un valor 
        yield x * 10, True #podemos devolver dos valores
    
#colocamos x , y porque en tield indicamos que devolveria dos valores
for x, y in generator(1, 2, 3, 4, 5 ,6 ,7 ,8, 9):
    print(x, y)