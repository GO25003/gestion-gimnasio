from repositorio_inscripciones import cargar_inscripciones, guardar_inscripciones
from servicio_miembros import buscar_miembro_por_id
from servicio_clases import buscar_clase_por_id
from repositorio_clases import cargar_clases, guardar_clases

def inscribir_miembro(id_miembro, id_clase):

    # 🔹 Validar que el miembro exista (Diego)
    miembro = buscar_miembro_por_id(id_miembro)
    if miembro is None:
        return "El miembro no existe."

    # 🔹 Validar que la clase exista (Johana)
    clase = buscar_clase_por_id(id_clase)
    if clase is None:
        return "La clase no existe."

    # 🔹 Verificar cupo disponible
    inscripciones = cargar_inscripciones()
    cantidad_inscritos = sum(1 for i in inscripciones if i["id_clase"] == id_clase)

    if cantidad_inscritos >= clase.capacidad_maxima:
        return "No hay cupo disponible en esta clase."

    # 🔹 Guardar inscripción
    nueva_inscripcion = {
        "id_miembro": id_miembro,
        "id_clase": id_clase
    }

    inscripciones.append(nueva_inscripcion)
    guardar_inscripciones(inscripciones)

    return "Inscripción realizada con éxito."