# Figura del arco para que el usuario pueda ver, de manera más gráfica, dónde va a patear y dónde va a tirarse
import random

figura_arco: str = """
    ___________________________________
    | 1               2               3 |
    |                                   |
    | 4               5               6 |
    |                                   |
    | 7               8               9 |
    """

# Medalla de oro para mostrar al final de la tanda de penales
figura_medalla_primer_lugar: str = """
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


def mostrar_resultado_final(goles_argentina, goles_paises_bajos):
    """Método para mostrar el resultado final del partido y la medalla para el equipo ganador."""
    equipo_ganador = ("Argentina", goles_argentina) \
        if goles_argentina > goles_paises_bajos \
        else ("Países Bajos", goles_paises_bajos)
    equipo_perdedor = ("Países Bajos", goles_argentina) \
        if not goles_argentina > goles_paises_bajos \
        else ("Argentina", goles_paises_bajos)
    print(f"""

    ---------------------------------

    Relator: ¡{equipo_ganador[0]} gana el partido y se lleva la medalla de oro!

    El partido terminó 0-0 y lo gana {equipo_ganador[0]} en penales,
    con puntaje de {equipo_ganador[1]} contra {equipo_perdedor[1]} puntos de {equipo_perdedor[0]}

    {figura_medalla_primer_lugar}
    """)


def calcular_penales(goles_argentina: int, goles_paises_bajos: int, numero_turnos: int):
    """Función para la tanda de penales.

    Se juegan 5 penales por equipo y, si un equipo mete más penales que el otro, gana el partido."""

    print("""

    ¡Comienzan los penales entre Argentina y Países Bajos!

    """)
    # Se usa el for para que cada vez que i % 2 == 0, signifique que ya ambos equipos tuvieron su turno
    for i in range(1, numero_turnos, 1):
        pais_atacante = "Argentina" if i % 2 == 0 else "Paises Bajos"
        pais_defensor = "Paises Bajos" if i % 2 != 0 else "Argentina"
        print(f"""

        Relator: Se prepara la jugadora de {pais_atacante}...

        Elige dónde vas a patear:

        {figura_arco}
        """)

        if pais_atacante == "Argentina":
            goles_argentina += calcular_cuadrantes_penal(elegir_cuadrante(), random.randint(1, 9))
        else:
            goles_paises_bajos += calcular_cuadrantes_penal(random.randint(1, 9), elegir_cuadrante())

        print(f"""

        ------ Argentina {goles_argentina} - Países Bajos {goles_paises_bajos} ------

        """)

        print(f"""

        Relator: Se prepara la jugadora de {pais_defensor}...

        Elige dónde vas a tirarte:

        {figura_arco}
        """)

        if pais_atacante == "Argentina":
            goles_argentina += calcular_cuadrantes_penal(elegir_cuadrante(), random.randint(1, 9))
        else:
            goles_paises_bajos += calcular_cuadrantes_penal(random.randint(1, 9), elegir_cuadrante())

        # Lógica para determinar si alguno de los países gana antes de que se termine la tanda de penales.
        if (goles_paises_bajos > goles_argentina + (4 - i // 2)) or (
                goles_argentina > goles_paises_bajos + (4 - i // 2)):
            print("""

            Relator: ¡Se terminó!

            """)
            return goles_argentina, goles_paises_bajos

        print(f"""

        ------ Argentina {goles_argentina} - Países Bajos {goles_paises_bajos} ------

        """)

    return goles_argentina, goles_paises_bajos


def calcular_cuadrantes_penal(cuadrante_ataque, cuadrante_defensa):
    """ Función que determina si el penal fue gol o atajado."""
    if cuadrante_ataque != cuadrante_defensa:
        print("""

        ---------------------------------

        Relator: Va a patear...

        ¡Gol! ¡Gol! ¡Gol! ¡Gol! ¡Gol!
        """)
        return 1
    else:
        print("""

        ---------------------------------

        Relator: Va a patear...

        ¡Atajó la arquera!
        """)
        return 0


def elegir_cuadrante():
    """Función para que el usuario elija dónde patear y tirarse en la tanda de penales junto con una validación para
    evitar errores al introducir un número fuera del rango de 1 a 9."""
    while True:
        try:
            decision = int(input("Ingrese el número del cuadrante a elegir:"))
            if decision < 1 or decision > 9:
                raise ValueError
            return decision
        except ValueError:
            print("Error. Ingrese un número válido entre 1 y 9")


if __name__ == '__main__':
    puntaje_argentina = 0
    puntaje_paises_bajos = 0
    puntaje_argentina, puntaje_paises_bajos = calcular_penales(puntaje_argentina, puntaje_paises_bajos, 11)

    # En caso de que ambos equipos hayan metido la misma cantidad de penales, se llama a la función
    # "definir_penales" para que se patee un penal por equipo hasta que haya un ganador. De lo contrario,
    # se determina el ganador del partido.
    if puntaje_argentina == puntaje_paises_bajos:
        # definir_penales(puntaje_argentina, puntaje_paises_bajos)
        while puntaje_argentina == puntaje_paises_bajos:
            puntaje_argentina, puntaje_paises_bajos = calcular_penales(puntaje_argentina, puntaje_paises_bajos, 2)
    else:
        mostrar_resultado_final(puntaje_argentina, puntaje_paises_bajos)
    print("")
