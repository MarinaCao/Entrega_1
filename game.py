import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
MAX_FAILURES = 10
# Inicializar en 0 el número de fallos
FAILURE_COUNT = 0
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
# Se elige la dificultad
while True:
    difficulty = input("Elige un nivel de dificultad (fácil/media/difícil): ").lower()
    if difficulty in ["fácil", "media", "difícil"]:
        break
    else:
        print("Opción inválida. Por favor, elige una de las opciones disponibles.")
# Obtener la palabra según el nivel de dificultad
if difficulty == "fácil":
    # Se muestran todas las vocales por defecto
    secret_word = random.choice(words)
    word_displayed = ""
    for letter in secret_word:
        if letter in "aeiou":
            word_displayed += letter
        else:
            word_displayed += "_"
elif difficulty == "media":
    # Se muestra la primera y la última letra de la palabra
    secret_word = random.choice(words)
    word_displayed = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]
elif difficulty == "difícil":
    # No se muestra ninguna letra de la palabra
    secret_word = random.choice(words)
    word_displayed = "_" * len(secret_word)
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
while FAILURE_COUNT < MAX_FAILURES:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()    
    # Verificar si la entrada está vacía
    if not letter:
        print("Error. No se ingresó ninguna letra. Intenta de nuevo.")
        continue    
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue    
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)  
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        FAILURE_COUNT += 1
        print(f"Tienes {FAILURE_COUNT} fallos de {MAX_FAILURES} permitidos.")
        print("Lo siento, la letra no está en la palabra.")
    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")  
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
    elif FAILURE_COUNT == MAX_FAILURES:
        print("¡Oh no! Has alcanzado el número máximo de fallos.")
        print(f"La palabra secreta era: {secret_word}")
        break