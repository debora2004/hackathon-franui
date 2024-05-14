import csv


def calcular_porcentaje(pases_bien: int, cantidad_pases: int) -> float:
    """
    Calcula el porcentaje de un registro de la lista, y requiere los siguientes argumentos:
        pases_bien: la cantidad de pases buenos
        cantidad_pases: el total de pases efectuados

    Devuelve el porcentaje de pases buenos
    """
    return (pases_bien / cantidad_pases) * 100


def crear_registro(registro_archivo: dict) -> dict:
    """
    Crea el registro de la lista de jugadoras, y requiere el siguiente argumento:
        registro_archivo: el registro del archivo, del cual se tomará el número y nombre de la jugadora

    Devuelve un registro en el formato solicitado y todos sus valores inicializados
    """
    return {'numero': registro_archivo['numero'],
            'nombre': registro_archivo['nombre'],
            'cantidad_pases': 0,
            'pases_bien': 0,
            'pases_mal': 0}


def actualizar_registro(registro_archivo: dict, registro_lista: dict) -> None:
    """
    Actualiza, en un registro, la cantidad de pases, los pases buenos o malos, y el porcentaje de pases buenos,
    y requiere los siguientes argumentos:
        registro_archivo: el registro que viene del archivo leído, del cuál se sacará la información necesaria
        registro_lista: el registro de la lista que será actualizado con la información del argumento anterior
    """
    registro_lista['cantidad_pases'] += 1
    if registro_archivo['hizo_pase'] == '1':
        registro_lista['pases_bien'] += 1
    else:
        registro_lista['pases_mal'] += 1
    registro_lista['porcentaje'] = round(calcular_porcentaje(registro_lista['pases_bien'],
                                                             registro_lista['cantidad_pases']), 2)


def contar_pases_y_efectividad(nombre_archivo: str, delimitador: str = ';'):
    """
    Lee el archivo y devuelve la información con el formato solicitado. Requiere el siguiente argumento:
        nombre_archivo: el nombre del archivo a leer.
        delimitador: el delimitador para los registros. Por defecto es un punto y coma

    El archivo debe estar en la misma carpeta en la que se corre este script.
    """
    datos_lista_argentina: dict[str, dict] = {}
    datos_lista_australia: dict[str, dict] = {}

    with open(nombre_archivo, encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo, delimiter=delimitador,
                                fieldnames=['pais', 'nombre', 'numero', 'hizo_pase'])
        for registro_archivo in reader:
            archivo_numero = registro_archivo['numero']
            if registro_archivo['pais'] == 'Argentina':
                if archivo_numero not in datos_lista_argentina:
                    datos_lista_argentina[archivo_numero] = crear_registro(registro_archivo)
                actualizar_registro(registro_archivo, datos_lista_argentina[archivo_numero])
            else:
                if archivo_numero not in datos_lista_australia:
                    datos_lista_australia[archivo_numero] = crear_registro(registro_archivo)
                actualizar_registro(registro_archivo, datos_lista_australia[archivo_numero])
    return [{'Argentina': sorted(datos_lista_argentina.values(), key=lambda jugadora: jugadora['porcentaje'], reverse=True)},
            {'Australia': sorted(datos_lista_australia.values(), key=lambda jugadora: jugadora['porcentaje'], reverse=True)}]


if __name__ == '__main__':
    # Se invoca el método que lee el archivo, con el nombre que deseemos
    print(contar_pases_y_efectividad('pases.txt'))

    # Benchmark
    # print(timeit.timeit('leer_archivo("pases.txt")', number=10000, setup="from __main__ import leer_archivo"))
