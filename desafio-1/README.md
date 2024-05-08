# Desafío: Registro de Eventos de Pases
Este proyecto consiste en un generador de datos de pases para equipos de hockey.

## Requisitos Previos

Para poder ejecutar este desafío, asegúrate de tener instalado Python en tu sistema. Si aún no lo tienes, puedes descargarlo desde el siguiente enlace: [Descargar Python](https://www.python.org/downloads/)


## Instrucciones de Ejecución

1. **Clonar el Repositorio**: Clonar este repositorio en tu máquina local.

    ```bash
    git clone https://github.com/tu_usuario/desafio-hockey.git
    ```

2. **Acceder al Directorio del Proyecto**: Navegar hasta el directorio donde clonaste el repositorio.

    ```bash
    cd desafio-hockey
    ```

3. **Ejecutar el Generador de Pases**: Utilizar el siguiente comando para ejecutar el generador de pases.

    ```bash
    python3 desafio1.py
    ```

## Sobre el Código

El código fuente se encuentra en el archivo `desafio1.py`. Este script Python genera datos simulados de pases entre jugadoras de equipos de hockey: Argentina vs Australia. 

### Funciones principales

- **`crear_datos(numero_de_datos: int) -> list[str]`**: Esta función crea datos simulados de pases entre jugadoras. Toma un argumento `numero_de_datos`, que indica el número máximo de registros a crear, y devuelve una lista de strings con los datos generados.

- **`crear_archivo(nombre_archivo: str, numero_de_datos: int) -> None`**: Esta función crea un archivo de texto para almacenar los datos generados. Toma dos argumentos: `nombre_archivo`, que es el nombre del archivo a crear (o sobrescribir si ya existe), y `numero_de_datos`, que es el número máximo de registros que se desean crear.

## Integrantes

- Abigail Justiniano: ajustiniano@uade.edu.ar
- Franco Barrera: Fbarrera@uade.edu.ar
- José Sierra: jsierra@uade.edu.ar
- Daniel Vidal: dvidalasto@uade.edu.ar
- Agustin Sanfilippo Kusmuk: asanfilippo@uade.edu.ar