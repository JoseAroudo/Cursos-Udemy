import random


def Main():
    listName=["jose","manzana","popular","hello","apple","alberto"]
    LetrasIngresadas = []

    palabra= random.choice(listName)
    numberLetters= len(list(palabra))#Number of letters that have a word and with that numbre put the "-" in the client
    print("-" * numberLetters)  # The word in indden mode

    vida = 5  # The life that the user have


    letra=input("Ingrese la letra: ")#This is the letter in orden to search

    # AGREGAR LETRAS DIGITADAS ANTERIORMENTE
    add_to_list = lambda Lista, letra: Lista.append(letra)  # Funtion para agregar letras al final

    #VALIDACIONES PARA SABER SI ES UNA LETRA VALIDAXD
    validar = lambda x: x.isalpha() and len(list(x)) == 1 and x not in LetrasIngresadas  # Validation to know if it is alphabet and is one letter
    # SABER DONDE ESTA LA LETRA
    posicion = lambda let, pal: pal.find(letra) if validar(let) and let in pal else -1
    print(f"lista de letras: {LetrasIngresadas}, validar: {validar(letra)}, posicion {posicion}")
    print(posicion(letra, palabra))






    add_to_list(LetrasIngresadas,letra)


Main()
#vida = lambda x: x > 0 para saber si tiene vidas todavia o no