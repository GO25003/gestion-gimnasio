import json
import os

RUTA = "datos/asistencias.json"

def cargar_asistencias():
    if not os.path.exists(RUTA):
        return []

    with open(RUTA, "r") as archivo:
        return json.load(archivo)

def guardar_asistencias(lista_asistencias):
    with open(RUTA, "w") as archivo:
        json.dump(lista_asistencias, archivo, indent=4)