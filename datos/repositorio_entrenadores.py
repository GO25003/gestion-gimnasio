import json
import os
from modelos.entrenador import Entrenador

ENTRENADORES_FILE = os.path.join(os.path.dirname(__file__), "entrenadores.json")

def cargar_entrenadores():
    if not os.path.exists(ENTRENADORES_FILE):
        return []
    with open(ENTRENADORES_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Entrenador(**item) for item in data]

def guardar_entrenadores(lista_entrenadores):
    data = [e.a_diccionario() for e in lista_entrenadores]
    with open(ENTRENADORES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)