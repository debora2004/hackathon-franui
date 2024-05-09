import random

"""
Para el desarrollo de esta actividad fueron consideradas las reglas oficiales de hockey césped femenino en los Juegos Olímpicos 2024.
También se utiliza el plantel oficial de las jugadoras de la selección Argentina y de Australia en el campeonato "Hockey Pro League femenina 2023-24".
Sitios de referencia:
https://olympics.com/es/paris-2024/deportes/hockey-sobre-cesped
https://olympics.com/es/noticias/hockey-tiempo-juego-jugadores-cancha-posiciones 
https://es.wikipedia.org/wiki/Hockey_Pro_League_femenina_2023-24
"""

# Dos tuplas que contienen el nombre del país y la lista de tuplas de jugadoras que lo representan
lista_jugadoras_argentina: tuple[str, list[tuple[str, int]]] = (
    "Argentina", [("Sofía Toccalino", 2), ("Agustina Gorzelany", 3), ("Valentina Raposo", 4), ("Agostina Alonso", 5),
                  ("Agustia Albertarrio", 7), ("María Granatto", 10), ("Cristina Cosentino", 13), ("Clara Barberi", 14),
                  ("Bárbara Dichiara", 16), ("Rocío Sánchez", 17), ("Victoria Sauze", 18), ("Victoria Manuele", 19),
                  ("Eugenia Trinchinetti", 22), ("María Campoy", 26), ("Julieta Jankunas", 28),
                  ("Stefanía Antoniazzi", 36), ("Juana Castellaro", 50), ("Lara Casas", 61)])
lista_jugadoras_australia: tuple[str, list[tuple[str, int]]] = (
    "Australia",
    [("Claire Colwill", 1), ("Ambrosia Malone", 2), ("Amy Lawton", 4), ("Grace Young", 5), ("Maddison Brooks", 8),
     ("Alice Arnott", 11), ("Hattie Shand", 13), ("Stephanie Kershaw", 14), ("Kaitlin Nobbs", 15), ("Lucy Sharman", 17),
     ("Jane Claxton", 18), ("Jocelyn Bartram", 19), ("Karri Somerville", 20), ("Renee Taylor", 21),
     ("Tatum Stewart", 22), ("Rebecca Greiner", 29), ("Grace Stewart", 30), ("Zoe Newman", 41)])


def crear_datos(numero_de_datos: int) -> list[str]:
    """
    Se crean, una por una, las strings que serán escritas al documento, con el siguiente argumento:

        numero_de_datos: el número máximo de registros que se deseen crear.

    Devuelve una lista de strings con los datos creados y con el formato solicitado.
    """
    datos: list[str] = []
    for i in range(numero_de_datos):
        lista_elegida: tuple[str, list[tuple[str, int]]] = random.choice(
            [lista_jugadoras_argentina, lista_jugadoras_australia])
        jugadora_elegida: tuple[str, int] = random.choice(lista_elegida[1])
        datos.append(f"{lista_elegida[0]};"
                     f"{jugadora_elegida[0]};"
                     f"{jugadora_elegida[1]};"
                     f"{(random.randint(0, 1))};"
                     f"{(random.randint(1, 60))}")
    return datos


def crear_archivo(nombre_archivo: str, numero_de_datos: int) -> None:
    """
    Se crea el archivo en el que se guardarán los datos con los siguientes argumentos:

        nombre_archivo: el nombre del archivo a crear. Si no existe, será creado. Si existe, será sobrescrito.
        numero_de_datos: el número máximo de registros que se deseen crear.

    El archivo creado será almacenado en la misma carpeta donde se corra este script.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(crear_datos(numero_de_datos)))


if __name__ == '__main__':
    # Se invoca el método que crea los archivos, con los argumentos que deseemos
    crear_archivo("pases.txt", 50000)
