import json
import os

RUTA = "datos/inscripciones.json"

def cargar_inscripciones():
    if not os.path.exists(RUTA):
        return []
    with open(RUTA, "r") as archivo:
        return json.load(archivo)

def guardar_inscripciones(inscripcion):
    inscripciones = cargar_inscripciones()
    inscripciones.append(inscripcion)
    with open(RUTA, "w") as archivo:
        json.dump(inscripciones, archivo, indent=4)