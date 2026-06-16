from datos.repositorio_clases import (
    cargar_clases,
    guardar_clases
)

from datos.repositorio_entrenadores import (
    cargar_entrenadores
)

from modelos.clase import Clase


def crear_clase(
    nombre_disciplina,
    horario,
    capacidad_maxima,
    entrenador
):
    if not nombre_disciplina or not nombre_disciplina.strip():
        raise ValueError(
            "El nombre de la disciplina no puede estar vacío."
        )

    if (
        not isinstance(capacidad_maxima, int)
        or capacidad_maxima <= 0
    ):
        raise ValueError(
            "La capacidad debe ser un número entero positivo."
        )

    entrenadores = cargar_entrenadores()

    existe = any(
        e.nombre.lower() == entrenador.lower()
        for e in entrenadores
    )

    if not existe:
        raise ValueError(
            "El entrenador indicado no existe."
        )

    clases = cargar_clases()

    nuevo_id = len(clases) + 1

    nueva_clase = Clase(
        nuevo_id,
        nombre_disciplina.strip(),
        horario.strip(),
        capacidad_maxima,
        entrenador.strip()
    )

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


def actualizar_clase(
    id_clase,
    nuevo_nombre=None,
    nuevo_horario=None,
    nueva_capacidad=None,
    nuevo_entrenador=None
):
    clases = cargar_clases()

    for clase in clases:

        if clase.id_clase == id_clase:

            if nuevo_nombre and nuevo_nombre.strip():
                clase.nombre_disciplina = nuevo_nombre.strip()

            if nuevo_horario and nuevo_horario.strip():
                clase.horario = nuevo_horario.strip()

            if nueva_capacidad is not None:

                if (
                    not isinstance(nueva_capacidad, int)
                    or nueva_capacidad <= 0
                ):
                    raise ValueError(
                        "La capacidad debe ser un número entero positivo."
                    )

                clase.capacidad_maxima = nueva_capacidad

            if nuevo_entrenador:

                entrenadores = cargar_entrenadores()

                existe = any(
                    e.nombre.lower()
                    == nuevo_entrenador.lower()
                    for e in entrenadores
                )

                if not existe:
                    raise ValueError(
                        "El entrenador indicado no existe."
                    )

                clase.entrenador = nuevo_entrenador.strip()

            guardar_clases(clases)

            return clase

    return None


def eliminar_clase(id_clase):
    clases = cargar_clases()

    nuevas = [
        c
        for c in clases
        if c.id_clase != id_clase
    ]

    if len(nuevas) == len(clases):
        return False

    guardar_clases(nuevas)

    return True