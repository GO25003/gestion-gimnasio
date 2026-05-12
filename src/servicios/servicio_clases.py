from datos.repositorio_clases import cargar_clases, guardar_clases
from modelos.clase import Clase

def crear_clase(nombre_disciplina, horario, capacidad_maxima):
    if not isinstance(capacidad_maxima, int) or capacidad_maxima <= 0:
        raise ValueError("La capacidad debe ser un número entero positivo.")
    clases = cargar_clases()
    nuevo_id = len(clases) + 1
    nueva_clase = Clase(nuevo_id, nombre_disciplina, horario, capacidad_maxima)
    clases.append(nueva_clase)
    guardar_clases(clases)
    return nueva_clase

def listar_clases():
    return cargar_clases()

def buscar_clase_por_id(id_clase):
    for c in cargar_clases():
        if c.id_clase == id_clase:
            return c
    return None