from datos.repositorio_entrenadores import cargar_entrenadores, guardar_entrenadores
from modelos.entrenador import Entrenador

def registrar_entrenador(nombre, especialidad):
    if not nombre or not nombre.strip():
        raise ValueError("El nombre del entrenador no puede estar vacío.")
    entrenadores = cargar_entrenadores()
    nuevo_id = len(entrenadores) + 1
    nuevo_entrenador = Entrenador(nuevo_id, nombre.strip(), especialidad)
    entrenadores.append(nuevo_entrenador)
    guardar_entrenadores(entrenadores)
    return nuevo_entrenador

def listar_entrenadores():
    return cargar_entrenadores()