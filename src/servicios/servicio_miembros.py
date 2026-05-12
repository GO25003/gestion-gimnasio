from repositorio_miembros import cargar_miembros, guardar_miembros
from miembro import Miembro


def registrar_miembro(nombre, apellido, email):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")

    miembros = cargar_miembros()

    nuevo_id = len(miembros) + 1

    nuevo_miembro = Miembro(nuevo_id, nombre, apellido, email)

    miembros.append(nuevo_miembro)

    guardar_miembros(miembros)

    return nuevo_miembro


def listar_miembros():
    return cargar_miembros()


def buscar_miembro_por_id(id_miembro):
    miembros = cargar_miembros()

    for miembro in miembros:
        if miembro.id_miembro == id_miembro:
            return miembro

    return None
