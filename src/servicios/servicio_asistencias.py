from datetime import datetime
from datos.repositorio_asistencias import cargar_asistencias, guardar_asistencias
from datos.repositorio_inscripciones import cargar_inscripciones

def registrar_asistencia(id_miembro, id_clase):

    inscripciones = cargar_inscripciones()

    # 🔹 Verificar inscripción previa
    inscrito = any(
        i["id_miembro"] == id_miembro and i["id_clase"] == id_clase
        for i in inscripciones
    )

    if not inscrito:
        return "El miembro no está inscrito en esta clase."

    asistencias = cargar_asistencias()

    nueva_asistencia = {
        "id_miembro": id_miembro,
        "id_clase": id_clase,
        "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    asistencias.append(nueva_asistencia)
    guardar_asistencias(asistencias)

    return "Asistencia registrada correctamente."
