import random

"""
Equipo 11: Franui

Desafío 3.

"El partido que define la medalla de oro entre Argentina y Países Bajos terminó empatado
sin goles y deberá definirse el ganador por la tanda de los penales. Deberá desarrollar un 
juego que le permita competir contra la computadora (Países Bajos) en una tanda de 
penales."
"""

# Figura del arco para que el usuario pueda ver, de manera más gráfica, dónde va a patear y dónde va a tirarse
def figuraarco():
    
    return """
  ___________________________________
 | 1               2               3 |
 |                                   |
 | 4               5               6 |
 |                                   |
 | 7               8               9 |
    """

    

# Medalla de oro para mostrar al final de la tanda de penales
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

# Print para mostrar el resultado final del partido y la medalla de oro.
def printresultadofinal(argentinagoles, paisesbajosgoles):
    if argentinagoles > paisesbajosgoles:
        print(" ")
        print("---------------------------------")
        print(" ")
        print("Relator: ¡Argentina gana el partido y se lleva la medalla de oro!")
        print("El partido terminó 0-0 y lo gana Argentina en penales", argentinagoles, "a", paisesbajosgoles, "ante Paises Bajos")
        print(medalladeoro())
    else:
        print(" ")
        print("---------------------------------")
        print(" ")
        print("Relator: ¡Países Bajos gana el partido y se lleva la medalla de oro!")
        print("El partido terminó 0-0 y lo gana Países Bajos en penales", paisesbajosgoles, "a", argentinagoles, "ante Argentina")
        print(medalladeoro())


# Función para la tanda de penales. Se juegan 5 penales por equipo. En esta instancia si un equipo mete más penales que el otro, gana el partido.
def penales():
    argentinagoles = 0
    paisesbajosgoles = 0

    print(" ")
    print("¡Comienzan los penales entre Argentina y Países Bajos!")
    # Uso del "for" para limitar la cantidad de penales a 5 por equipo
    for i in range(5):
        print(" ")  
        print("Relator: Se prepara la jugadora argentina...")
        print(" ")
        print("Elige dónde vas a patear")
        print(" ")
        print(figuraarco())
        decisionargentina = decision()
        decisionpaisesbajos = random.randint(1,9)
        tiradora = decisionargentina
        arquera = decisionpaisesbajos
        argentinagoles += funcionamientopenales(tiradora, arquera)

        # Lógica para determinar si Argentina gana antes de que termine la primer tanda de penales
        if argentinagoles > paisesbajosgoles + (4 - i):
            print(" ")
            print("Relator: ¡Se terminó!")
            return argentinagoles, paisesbajosgoles

        print(" ")
        print("------ Argentina", argentinagoles, "- Países Bajos", paisesbajosgoles, "------")

        print(" ")
        print("Relator: Va a patear Países Bajos")  
        print(" ")
        print("Relator: Se prepara la jugadora de Países Bajos...")
        print(" ")
        print("Elige dónde vas a tirarte")
        print(" ")
        print(figuraarco())
        decisionargentina = decision()
        decisionpaisesbajos = random.randint(1,9)
        tiradora = decisionpaisesbajos
        arquera = decisionargentina
        paisesbajosgoles += funcionamientopenales(tiradora, arquera)

        # Lógica para determinar si Países Bajos gana antes de que termine la primer tanda de penales
        if paisesbajosgoles > argentinagoles + (4 - i):
            print(" ")
            print("Relator: ¡Se termíno!")
            return argentinagoles, paisesbajosgoles


        print(" ")
        print("------ Argentina", argentinagoles, "- Países Bajos", paisesbajosgoles, "------")

    return argentinagoles, paisesbajosgoles

# En caso de que el partido termine empatado en la primer tanda de penales, se patea de a un penal por equipo.
def definicionpenales(argentinagoles, paisesbajosgoles):
    while argentinagoles == paisesbajosgoles:
        print(" ")
        print("Relator: Va a patear Argentina")
        print(" ")
        print("Relator: Se prepara la jugadora argentina...")
        print(" ")
        print("Elige dónde vas a patear")
        print(" ")
        print(figuraarco())
        decisionargentina = decision()
        decisionpaisesbajos = random.randint(1,9)
        tiradora = decisionargentina
        arquera = decisionpaisesbajos
        resultado = funcionamientopenales(tiradora, arquera)
        argentinagoles += resultado

        # Permite contextualizar al usuario sobre la situación del partido y también ajusta el valor de la variable "fin".
        if resultado == 1:
            print(" ")
            print("Relator: Tiene que meter sí o sí Países Bajos si quiere seguir en el partido")
            fin = 1
        else:
            print(" ")
            print("Relator: ¡Si Países Bajos mete el siguiente penal es el ganador!")
            fin = 0

        print(" ")
        print("Relator: Va a patear Países Bajos")  
        print(" ")
        print("Relator: Se prepara la jugadora de Países Bajos...")
        print(" ")
        print("Elige dónde vas a tirarte")
        print(" ")
        print(figuraarco())
        decisionargentina = decision()
        decisionpaisesbajos = random.randint(1,9)
        tiradora = decisionpaisesbajos
        arquera = decisionargentina
        resultado = funcionamientopenales(tiradora, arquera)
        paisesbajosgoles += resultado

        # Determina si se sigue pateando penales o si terminó el partido.
        if (resultado == 1 and fin == 1) or (resultado == 0 and fin == 0):
            print(" ")
            print("Relator: ¡Siguen los penales!")
        elif (resultado == 1 and fin == 0) or (resultado == 0 and fin == 1):
            printresultadofinal(argentinagoles, paisesbajosgoles)
            break

# Función que determina si el penal fue gol o atajado.
def funcionamientopenales(tiradora, arquera):
    if (tiradora in [1, 4, 7] and arquera not in [1, 4, 7]) or (tiradora in [2, 5, 8] and arquera not in [2, 5, 8]) or (tiradora in [3, 6, 9] and arquera not in [3, 6, 9]):
        print(" ")
        print("---------------------------------")
        print(" ")
        print("Relator: Va a patear...")
        print("¡Gol! ¡Gol! ¡Gol! ¡Gol! ¡Gol!")
        return 1
    else:
        print(" ")
        print("---------------------------------")
        print(" ")
        print("Relator: Va a patear...")
        print("¡Atajó la arquera!")
        return 0

# Función para que el usuario elija dónde patear y tirarse en la tanda de penales junto con una validación para evitar errores al introducir un número fuera del rango de 1 a 9.
def decision():
    while True:
        try:
            decision = int(input("Número:"))
            if decision < 1 or decision > 9:
                raise ValueError
            return decision
        except ValueError:
            print("Error. Ingrese un número válido entre 1 y 9")

# Llama a la función "penales" para que se ejecute la tanda de penales.
argentinagoles, paisesbajosgoles = penales()

# En caso de que ambos equipos hayan metido la misma cantidad de penales, se llama a la función "definicionpenales" para que se patee un penal por equipo hasta que haya un ganador. De lo contrario, se determina el ganador del partido.
if argentinagoles == paisesbajosgoles:
    definicionpenales(argentinagoles, paisesbajosgoles)
else:
    printresultadofinal(argentinagoles, paisesbajosgoles)


