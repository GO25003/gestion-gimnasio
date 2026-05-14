
from datos.repositorio_miembros import cargar_miembros, guardar_miembros
from modelos.miembro import Miembro


def registrar_miembro(nombre, apellido, email):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    if not email.strip():
        raise ValueError("El email no puede estar vacío.")

    miembros = cargar_miembros()

    nuevo_id = len(miembros) + 1
    nuevo_miembro = Miembro(nuevo_id, nombre.strip(), apellido.strip(), email.strip())

    miembros.append(nuevo_miembro)
    guardar_miembros(miembros)

    return nuevo_miembro


def listar_miembros():
    return cargar_miembros()


def buscar_miembro_por_id(id_miembro):
    for miembro in cargar_miembros():
        if miembro.id_miembro == id_miembro:
            return miembro
    return None


def actualizar_miembro(id_miembro, nuevo_nombre=None, nuevo_apellido=None, nuevo_email=None):
    miembros = cargar_miembros()

    for miembro in miembros:
        if miembro.id_miembro == id_miembro:
            if nuevo_nombre and nuevo_nombre.strip():
                miembro.nombre = nuevo_nombre.strip()
            if nuevo_apellido and nuevo_apellido.strip():
                miembro.apellido = nuevo_apellido.strip()
            if nuevo_email and nuevo_email.strip():
                miembro.email = nuevo_email.strip()

            guardar_miembros(miembros)
            return miembro

    return None


def eliminar_miembro(id_miembro):
    miembros = cargar_miembros()
    nuevos = [m for m in miembros if m.id_miembro != id_miembro]

    if len(nuevos) == len(miembros):
        return False  # No se encontró

    guardar_miembros(nuevos)
    return True