def funcion():
    numero=0
    while True:
        yield numero
        numero += 1


generador = funcion()

for i in range (10):
    print(next(generador))
print(next(generador))
