import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos(Se cambia a maximo de fallos)
MAX_FAILURES = 10
# Inicializo en 0 el número de fallos
FAILURE_COUNT= 0
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
while word_displayed != secret_word and FAILURE_COUNT < MAX_FAILURES:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
     # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    # Verifico que no sea vacio
    if not letter.isalpha():
        print("Error. No se ingreso ninguna letra intente de nuevo")
    # Verificar si la letra está en la palabra secreta
    else:
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            FAILURE_COUNT +=1
            print(f"Tienes {FAILURE_COUNT} fallos de {MAX_FAILURES} permitidos.")
            print("Lo siento, la letra no está en la palabra.")
 # Mostrar la palabra parcialmente adivinada
letters = []
for letter in secret_word:
    if letter in guessed_letters:
        letters.append(letter)
    else:
        letters.append("_")
    word_displayed= "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
    else:
        print(f"¡Oh no! Has agotado tus {MAX_FAILURES} intentos.")
        print(f"La palabra secreta era: {secret_word}")