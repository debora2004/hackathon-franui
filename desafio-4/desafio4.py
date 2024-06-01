import json
import random


def comenzar_preguntas(jugadores, nombre_archivo):
    pregunta = ""
    try:
        preguntas: dict = json.load(open(nombre_archivo))['preguntas']
    except FileNotFoundError:
        print("El archivo no fue encontrado, por favor verifique el nombre e intente de nuevo")

    for jugador in range(jugadores):
        print(f"""
        ¡Es el turno del jugador {jugador}
        """)

        pregunta = random.choice(preguntas)

        texto_pregunta = list(pregunta.keys())[0]

        texto_respuesta_a = list(list(pregunta.values())[0].keys())[0]
        texto_respuesta_b = list(list(pregunta.values())[0].keys())[1]
        texto_respuesta_c = list(list(pregunta.values())[0].keys())[2]

        respuesta_a = list(list(pregunta.values())[0].values())[0]
        respuesta_b = list(list(pregunta.values())[0].values())[1]
        respuesta_c = list(list(pregunta.values())[0].values())[2]

        print(f"""
        La pregunta es: {texto_pregunta}
        
        Las posibles opciones son:
        
        a - {texto_respuesta_a}
        b - {texto_respuesta_b}
        c - {texto_respuesta_c}
        """)



print("¡Bienvenidos al juego Preguntas y Respuestas Olímpicas!")


def medalladeoro():
    return """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⣾⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⢠⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⡿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣷⢿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⡜⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣿⣿⣷⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠉⠉⠉⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣿⣿⣿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠉⠀⠀⠀⠀⠀⠉⠻⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡟⠁⠀⠀⠀⢀⣀⣀⠀⠀⠀⠈⢻⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠀⠀⠀⠀⠸⢿⣿⣿⠀⠀⠀⠀⠀⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⡇⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⢸⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀⠀⠀⠀⠀⣸⣿⣿⠀⠀⠀⠀⠀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣧⡀⠀⠀⠘⠛⠛⠛⠃⠀⠀⢀⣼⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⣀⠀⠀⠀⠀⠀⣀⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⣿⣿⣿⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""


def competidores():
    # Valores de los competidores
    respuestascorrectas = 0
    usuario = respuestascorrectas
    rivaln1 = random.randint(0, 5)
    rivaln2 = random.randint(0, 5)
    rivaln3 = random.randint(0, 5)
    return usuario, rivaln1, rivaln2, rivaln3


def ganador(usuario, rivaln1, rivaln2, rivaln3):
    # Lógica para poder definir al ganador
    if usuario > rivaln1 and usuario > rivaln2 and usuario > rivaln3:
        print(f"¡El ganador es... El usuario con {usuario} respuestas correctas!")
        print(medalladeoro())
    elif rivaln1 > usuario and rivaln1 > rivaln2 and rivaln1 > rivaln3:
        print(f"¡El ganador es... Paulo Pérez con {rivaln1} respuestas correctas!")
        print(medalladeoro())
    elif rivaln2 > usuario and rivaln2 > rivaln1 and rivaln2 > rivaln3:
        print(f"¡El ganador es... Mariana Gomez con {rivaln2} respuestas correctas!")
        print(medalladeoro())
    elif rivaln3 > usuario and rivaln3 > rivaln1 and rivaln3 > rivaln2:
        print(f"¡El ganador es... Luciano Aimar con {rivaln3} respuestas correctas!")
        print(medalladeoro())
    else:
        print(
            f"Terminó en empate. ¡Vuelvan a intentarlo! Los resultados fueron: El usuario con {usuario} respuestas correctas, Paulo Pérez con {rivaln1} respuestas correctas, Mariana Gomez con {rivaln2} respuestas correctas y Luciano Aimar con {rivaln3} respuestas correctas")


def juego():
    # Lógica del juego
    respuestascorrectas = 0

    print("¡Comenzamos con las preguntas! Suerte a todos los participantes")

    for i in range(5):
        print("")
        respuesta = input("Respuesta: ")

        if respuesta == 'True':
            print("¡Respuesta correcta! Sumás un punto")
            respuestascorrectas += 1
        else:
            print("¡Respuesta incorrecta!")

        if i != 5:
            print("¡Siguiente pregunta!")
        elif i == 4:
            print("¡Última pregunta!")
        else:
            print("Terminaron las preguntas")
            print("")

        print("")

    usuario, rivaln1, rivaln2, rivaln3 = competidores()
    ganador(usuario, rivaln1, rivaln2, rivaln3)

def ingresar_valor(mensaje, tipo):
    while True:
        try:
            if tipo == 'int':
                resultado = int(input(mensaje + "\n"))
                break
            if tipo == 'str':
                resultado = str(input(mensaje + "\n"))
                break
        except ValueError:
            print(f"El valor introducido no es un {tipo}, por favor intenta de nuevo")
    return resultado


def inicializar_archivo(nombre_archivo: str) -> None:
    """
    Se crea el archivo en el que se guardarán los datos con los siguientes argumentos:

        nombre_archivo: el nombre del archivo a crear. Si no existe, será creado. Si existe, será sobrescrito.

    El archivo creado será almacenado en la misma carpeta donde se corra este script.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("")


def iniciar_juego():
    print("Iniciando juego X\n")

    print("""
    Seleccione con un número alguna de las opciones del juego:

    1 - Iniciar juego
    2 - Cargar preguntas
    """)

    opcion_seleccionada = int(input("Inserte la opción que desee usar\n"))

    if opcion_seleccionada == 1:
        jugadores = ingresar_valor("Ingrese número de jugadores:", "int")
        comenzar_preguntas(jugadores, "preguntas.json")
    # if opcion_seleccionada == 2:
    #     cargar_preguntas()


if __name__ == '__main__':
    iniciar_juego()
