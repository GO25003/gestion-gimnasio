import json
from modelos.miembro import Miembro

RUTA_ARCHIVO = "datos/miembros.json"


def cargar_miembros():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            miembros = []

            for item in datos:
                miembro = Miembro(
                    item["id_miembro"],
                    item["nombre"],
                    item["apellido"],
                    item["email"]
                )
                miembros.append(miembro)

            return miembros
    except FileNotFoundError:
        return []


def guardar_miembros(lista_miembros):
    datos = [miembro.a_diccionario() for miembro in lista_miembros]

    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)