import random

def obtener_palabra_aleatoria():
    palabras = ["python", "programacion", "ordenador", "desarrollo", "juego"]
    palabra = random.choice(palabras)
    return palabra

def mostrar_tablero(intentos, letras_adivinadas):
    print("\nIntentos restantes:", intentos)
    print("Letras adivinadas:", " ".join(letras_adivinadas))

def adivinar_letra(palabra, letras_adivinadas, letra):
    letras_correctas = 0
    for i in range(len(palabra)):
        if palabra[i] == letra:
            letras_adivinadas[i] = letra
            letras_correctas += 1
    return letras_correctas

def jugar_ahorcado():
    palabra = obtener_palabra_aleatoria()
    letras_adivinadas = ["_"] * len(palabra)
    intentos = 6
    letras_correctas = 0

    while intentos > 0 and letras_correctas < len(palabra):
        mostrar_tablero(intentos, letras_adivinadas)
        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1:
            print("Ingresa solo una letra.")
            continue

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue

        letras_encontradas = adivinar_letra(palabra, letras_adivinadas, letra)
        if letras_encontradas == 0:
            intentos -= 1
            print("¡Letra incorrecta!")
        else:
            letras_correctas += letras_encontradas
            print("¡Letra encontrada!")

    mostrar_tablero(intentos, letras_adivinadas)

    if letras_correctas == len(palabra):
        print("¡Felicidades! Has adivinado la palabra:", palabra)
    else:
        print("¡Oh no! Has agotado tus intentos. La palabra era:", palabra)

jugar_ahorcado()
