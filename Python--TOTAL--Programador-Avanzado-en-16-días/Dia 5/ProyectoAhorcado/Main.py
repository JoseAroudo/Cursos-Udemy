import random


def Main():
    listName=["jose","manzana","popular","hello","apple","alberto"]
    LetrasIngresadas = []

    palabra= random.choice(listName)
    numberLetters= len(list(palabra))#Number of letters that have a word and with that numbre put the "-" in the client
    hidden_word = "-" * numberLetters  # The word in hidden mode
    print(hidden_word)  # The word in hidden mode
    vida = 5  # The life that the user have


    # AGREGAR LETRAS DIGITADAS ANTERIORMENTE
    add_to_list = lambda Lista, letra: Lista.append(letra)  # Funtion para agregar letras al final
    #VALIDACIONES PARA SABER SI ES UNA LETRA VALIDAXD
    validar_letra = lambda x: x.isalpha() and len(list(x)) == 1 and x not in LetrasIngresadas  # Validation to know if it is alphabet and is one letter
    # SABER DONDE ESTA LA LETRA
    posiciones = lambda let, pal: [i for i, l in enumerate(pal) if l == let] if validar_letra(let) else []


    while vida > 0:
        if hidden_word == palabra:
            print(f"ganaste, la palabra era {palabra}")
            break
        letra=input("Ingrese la letra: ")#This is the letter in orden to search
        if validar_letra(letra) and letra in palabra:
            print("La letra esta en la palabra")
            for posicion in posiciones(letra, palabra):
                hidden_word = hidden_word[:posicion] + letra + hidden_word[posicion + 1:]
            print(hidden_word)
        else:
            print("La letra no esta en la palabra")
            vida -= 1
            print(f"Te quedan {vida} vidas")
        add_to_list(LetrasIngresadas, letra)




Main()