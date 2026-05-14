import json
import os

RUTA = "datos/inscripciones.json"


def cargar_inscripciones():
    if not os.path.exists(RUTA):
        return []

    with open(RUTA, "r") as archivo:
        contenido = archivo.read().strip()

        if not contenido:
            return []

        return json.loads(contenido)


def guardar_inscripciones(inscripciones):
    with open(RUTA, "w") as archivo:
        json.dump(inscripciones, archivo, indent=4)