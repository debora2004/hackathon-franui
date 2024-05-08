import random

# Dos tuplas que contienen el nombre del país y la lista de tuplas de jugadoras que lo representan
lista_jugadoras_argentina: tuple[str, list[tuple[str, int]]] = (
    "Argentina", [("Agustina Gorzelany", 11), ("Marı́a José Granatto", 9), ("Sofia Toccalino", 20),
                  ("Agostina Alonso", 10), ("Valentina Raposo", 8), ("Clara Barberi", 5),
                  ("Delfina Thome", 4), ("Sofia Cairó", 7), ("Pilar Campoy", 16)])
lista_jugadoras_australia: tuple[str, list[tuple[str, int]]] = (
    "Australia", [("Violet Hardy", 1), ("Sandra Graves", 5), ("Georgia Glover", 13), ("Ursa Freeman", 21),
                  ("Danielle Ruiz", 7), ("Sally Willis", 11), ("Ruby Anderson", 17), ("Rowena Craig", 90),
                  ("Faye Haynes", 88)])


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
                     f"{(random.randint(0, 90))}")
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
