import timeit


def calcular_porcentaje(pases_bien: int, cantidad_pases: int) -> float:
    """
    Calcula el porcentaje de un registro de la lista, y requiere los siguientes argumentos:
        pases_bien: la cantidad de pases buenos
        cantidad_pases: el total de pases efectuados

    Devuelve el porcentaje de pases buenos
    """
    return (pases_bien / cantidad_pases) * 100


def crear_registro(numero: str, nombre: str) -> dict:
    """
    Crea el registro de la lista de jugadoras, y requiere el siguiente argumento:
        registro_archivo: el registro del archivo, del cual se tomará el número y nombre de la jugadora

    Devuelve un registro en el formato solicitado y todos sus valores inicializados
    """
    return {'numero': numero,
            'nombre': nombre,
            'cantidad_pases': 0,
            'pases_bien': 0,
            'pases_mal': 0}


def actualizar_registro(hizo_pase: str, registro_lista: dict) -> None:
    """
    Actualiza, en un registro, la cantidad de pases, los pases buenos o malos, y el porcentaje de pases buenos,
    y requiere los siguientes argumentos:
        registro_archivo: el registro que viene del archivo leído, del cuál se sacará la información necesaria
        registro_lista: el registro de la lista que será actualizado con la información del argumento anterior
    """
    registro_lista['cantidad_pases'] += 1
    if hizo_pase == '1':
        registro_lista['pases_bien'] += 1
    else:
        registro_lista['pases_mal'] += 1
    registro_lista['porcentaje'] = round(calcular_porcentaje(registro_lista['pases_bien'],
                                                             registro_lista['cantidad_pases']), 2)


def contar_pases_y_efectividad(nombre_archivo: str) -> list[dict: [str, any]]:
    """
    Lee el archivo de texto y devuelve la información con el formato solicitado. 
    Requiere el siguiente argumento:
        nombre_archivo: el nombre del archivo a leer.

    El archivo debe estar en la misma carpeta en la que se corre este script.
    """
    datos_lista_argentina: dict[str, dict] = {}
    datos_lista_australia: dict[str, dict] = {}

    with open(nombre_archivo, encoding="utf-8") as archivo:
        for linea in archivo:
            campos = linea.strip().split(';')
            nombre = campos[1]
            numero = campos[2]
            hizo_pase = campos[3]
            if campos[0] == 'Argentina':
                if numero not in datos_lista_argentina:
                    datos_lista_argentina[numero] = crear_registro(numero, nombre)
                actualizar_registro(hizo_pase, datos_lista_argentina[numero])
            else:
                if numero not in datos_lista_australia:
                    datos_lista_australia[numero] = crear_registro(numero, nombre)
                actualizar_registro(hizo_pase, datos_lista_australia[numero])

    # Orden por porcentaje de mayor a menor
    return [{'Argentina': sorted(datos_lista_argentina.values(), key=lambda x: x['porcentaje'], reverse=True)},
            {'Australia': sorted(datos_lista_australia.values(), key=lambda x: x['porcentaje'], reverse=True)}]


if __name__ == '__main__':
    # Se invoca el método que lee el archivo, con el nombre que deseemos
    # print(contar_pases_y_efectividad('pases.txt'))

    # Benchmark
    print(timeit.timeit('contar_pases_y_efectividad("pases.txt")', number=1000000,
                        setup="from __main__ import contar_pases_y_efectividad"))
