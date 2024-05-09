# Desafío: Registro de Eventos de Pases

Este proyecto consiste en un generador de datos de pases para equipos de hockey.

## Requisitos Previos

Para poder ejecutar este desafío, asegúrate de tener instalado Python en tu sistema. Si aún no lo tienes, puedes
descargarlo desde el siguiente enlace, preferiblemente la última versión que esté disponible en el
momento: [Descargar Python](https://www.python.org/downloads/)

## Instrucciones de Ejecución

1. **Clonar el Repositorio**: Clona este repositorio en tu máquina local.

    ```bash
    git clone https://github.com/debora2004/hackathon-franui.git
    ```

2. **Acceder al Directorio del Proyecto**: Navega hasta el directorio donde clonaste el repositorio.

    ```bash
    cd desafio-1
    ```

3. **Ejecutar el Generador de Pases**: Utiliza el siguiente comando para ejecutar el generador de pases.

    ```bash
    python3 desafio1.py
    ```

## Sobre el Código

El código fuente se encuentra en el archivo `desafio1.py`. Este script de Python genera datos simulados de pases entre
jugadoras de equipos de hockey para el partido de Argentina vs Australia.

### Funciones principales

- **`crear_datos(numero_de_datos: int) -> list[str]`**: Esta función crea datos simulados de pases entre jugadoras. Toma
  un argumento `numero_de_datos`, que indica el número máximo de registros a crear, y devuelve una lista de strings con
  los datos generados.

- **`crear_archivo(nombre_archivo: str, numero_de_datos: int) -> None`**: Esta función crea un archivo de texto para
  almacenar los datos generados. Toma dos argumentos: `nombre_archivo`, que es el nombre del archivo a crear (o
  sobrescribir si ya existe), y `numero_de_datos`, que es el número máximo de registros que se desean crear.

## Integrantes

- [Abigail Justiniano](mailto:ajustiniano@uade.edu.ar)
- [Franco Barrera](mailto:fbarrera@uade.edu.ar)
- [José Sierra](mailto:jsierra@uade.edu.ar)
- [Daniel Vidal](mailto:dvidalasto@uade.edu.ar)
- [Agustin Sanfilippo Kusmuk](mailto:asanfilippo@uade.edu.ar)