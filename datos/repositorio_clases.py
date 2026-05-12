import json
import os
from modelos.clase import Clase

CLASES_FILE = os.path.join(os.path.dirname(__file__), "clases.json")

def cargar_clases():
    if not os.path.exists(CLASES_FILE):
        return []
    with open(CLASES_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Clase(**item) for item in data]

def guardar_clases(lista_clases):
    data = [clase.a_diccionario() for clase in lista_clases]
    with open(CLASES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)