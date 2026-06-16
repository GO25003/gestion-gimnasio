import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from servicios.servicio_miembros import (
    registrar_miembro, listar_miembros, buscar_miembro_por_id,
    actualizar_miembro, eliminar_miembro
)

from servicios.servicio_clases import (
    crear_clase, listar_clases, buscar_clase_por_id,
    actualizar_clase, eliminar_clase
)

from servicios.servicio_inscripciones import (
    inscribir_miembro, listar_inscripciones
)

from servicios.servicio_asistencias import (
    registrar_asistencia, cargar_asistencias, listar_asistencias
)

from servicios.servicio_entrenadores import (
    registrar_entrenador,
    listar_entrenadores,
    actualizar_entrenador,
    eliminar_entrenador
)

# ─────────────────────────────────────────────
#  UTILIDAD
# ─────────────────────────────────────────────

def separador(titulo=""):
    ancho = 40
    if titulo:
        print(f"\n{'─' * 4} {titulo} {'─' * (ancho - len(titulo) - 6)}")
    else:
        print("─" * ancho)


def pausar():
    input("\nPresione Enter para continuar...")


# ─────────────────────────────────────────────
#  MÓDULO: MIEMBROS
# ─────────────────────────────────────────────

def menu_miembros():
    while True:
        separador("MIEMBROS")
        print("  1. Registrar miembro")
        print("  2. Listar miembros")
        print("  3. Buscar miembro por ID")
        print("  4. Actualizar miembro")
        print("  5. Eliminar miembro")
        print("  0. ← Volver")

        try:
            opcion = int(input("\n  Opción: "))

            if opcion == 1:
                nombre   = input("  Nombre: ")
                apellido = input("  Apellido: ")
                email    = input("  Email: ")
                miembro  = registrar_miembro(nombre, apellido, email)
                print(f"  ✓ Miembro registrado con ID {miembro.id_miembro}.")

            elif opcion == 2:
                miembros = listar_miembros()
                if not miembros:
                    print("  Sin miembros registrados.")
                else:
                    separador("Lista de miembros")
                    for m in miembros:
                        print(f"  [{m.id_miembro}] {m.nombre} {m.apellido} — {m.email}")

            elif opcion == 3:
                id_miembro = int(input("  ID del miembro: "))
                miembro = buscar_miembro_por_id(id_miembro)
                if miembro:
                    print(f"  [{miembro.id_miembro}] {miembro.nombre} {miembro.apellido} — {miembro.email}")
                else:
                    print("  ✗ Miembro no encontrado.")

            elif opcion == 4:
                id_miembro = int(input("  ID del miembro a actualizar: "))
                miembro = buscar_miembro_por_id(id_miembro)
                if not miembro:
                    print("  ✗ Miembro no encontrado.")
                else:
                    print(f"  Actual: {miembro.nombre} {miembro.apellido} — {miembro.email}")
                    print("  (Deja en blanco para no modificar)")
                    nuevo_nombre   = input("  Nuevo nombre: ")
                    nuevo_apellido = input("  Nuevo apellido: ")
                    nuevo_email    = input("  Nuevo email: ")
                    actualizado = actualizar_miembro(
                        id_miembro,
                        nuevo_nombre   or None,
                        nuevo_apellido or None,
                        nuevo_email    or None,
                    )
                    print(f"  ✓ Actualizado: {actualizado.nombre} {actualizado.apellido} — {actualizado.email}")

            elif opcion == 5:
                id_miembro = int(input("  ID del miembro a eliminar: "))
                if eliminar_miembro(id_miembro):
                    print("  ✓ Miembro eliminado.")
                else:
                    print("  ✗ Miembro no encontrado.")

            elif opcion == 0:
                break
            else:
                print("  Opción inválida.")

        except ValueError as e:
            print(f"  Error de valor. Ingrese una opcion valida")
        except Exception as e:
            print(f"  Error inesperado: {e}")

        pausar()


# ─────────────────────────────────────────────
#  MÓDULO: CLASES
# ─────────────────────────────────────────────

def menu_clases():
    while True:
        separador("CLASES")
        print("  1. Crear clase")
        print("  2. Listar clases")
        print("  3. Buscar clase por ID")
        print("  4. Actualizar clase")
        print("  5. Eliminar clase")
        print("  0. ← Volver")

        try:
            opcion = int(input("\n  Opción: "))

            if opcion == 1:
                nombre = input("  Nombre de la disciplina: ")
                horario = input("  Horario (ej: Lunes 08:00): ")
                capacidad = int(input("  Capacidad máxima: "))
                entrenador = input("  Entrenador: ")

                clase = crear_clase(
                    nombre,
                    horario,
                    capacidad,
                    entrenador
                )

                print(
                    f"  ✓ Clase creada con ID "
                    f"{clase.id_clase}."
                )

            elif opcion == 2:
                clases = listar_clases()

                if not clases:
                    print("  Sin clases registradas.")
                else:
                    separador("Lista de clases")

                    for c in clases:
                        print(
                            f"  [{c.id_clase}] "
                            f"{c.nombre_disciplina} | "
                            f"{c.horario} | "
                            f"Cupo: {c.capacidad_maxima} | "
                            f"Entrenador: {c.entrenador}"
                        )

            elif opcion == 3:
                id_clase = int(
                    input("  ID de la clase: ")
                )

                clase = buscar_clase_por_id(
                    id_clase
                )

                if clase:
                    print(
                        f"  [{clase.id_clase}] "
                        f"{clase.nombre_disciplina} | "
                        f"{clase.horario} | "
                        f"Cupo: {clase.capacidad_maxima} | "
                        f"Entrenador: {clase.entrenador}"
                    )
                else:
                    print(
                        "  ✗ Clase no encontrada."
                    )

            elif opcion == 4:
                id_clase = int(
                    input(
                        "  ID de la clase a actualizar: "
                    )
                )

                clase = buscar_clase_por_id(
                    id_clase
                )

                if not clase:
                    print(
                        "  ✗ Clase no encontrada."
                    )
                else:

                    print(
                        f"  Actual: "
                        f"{clase.nombre_disciplina} | "
                        f"{clase.horario} | "
                        f"Cupo: {clase.capacidad_maxima} | "
                        f"Entrenador: {clase.entrenador}"
                    )

                    print(
                        "  (Deja en blanco para no modificar)"
                    )

                    nuevo_nombre = input(
                        "  Nuevo nombre de disciplina: "
                    )

                    nuevo_horario = input(
                        "  Nuevo horario: "
                    )

                    nueva_cap_str = input(
                        "  Nueva capacidad: "
                    )

                    nuevo_entrenador = input(
                        "  Nuevo entrenador: "
                    )

                    nueva_capacidad = (
                        int(nueva_cap_str)
                        if nueva_cap_str.strip()
                        else None
                    )

                    actualizada = actualizar_clase(
                        id_clase,
                        nuevo_nombre or None,
                        nuevo_horario or None,
                        nueva_capacidad,
                        nuevo_entrenador or None
                    )

                    print(
                        f"  ✓ Actualizada: "
                        f"{actualizada.nombre_disciplina} | "
                        f"{actualizada.horario} | "
                        f"Cupo: {actualizada.capacidad_maxima} | "
                        f"Entrenador: {actualizada.entrenador}"
                    )

            elif opcion == 5:
                id_clase = int(
                    input(
                        "  ID de la clase a eliminar: "
                    )
                )

                if eliminar_clase(id_clase):
                    print(
                        "  ✓ Clase eliminada."
                    )
                else:
                    print(
                        "  ✗ Clase no encontrada."
                    )

            elif opcion == 0:
                break

            else:
                print("  Opción inválida.")

        except ValueError as e:
            print(
                f"  Error: {e}"
            )

        except Exception as e:
            print(
                f"  Error inesperado: {e}"
            )

        pausar()

# ─────────────────────────────────────────────
#  MÓDULO: ENTRENADORES
# ─────────────────────────────────────────────

def menu_entrenadores():
    while True:
        separador("ENTRENADORES")
        print("  1. Registrar entrenador")
        print("  2. Listar entrenadores")
        print("  3. Actualizar entrenador")
        print("  4. Eliminar entrenador")
        print("  0. ← Volver")

        try:
            opcion = int(input("\n  Opción: "))

            if opcion == 1:
                nombre = input("  Nombre: ")
                especialidad = input("  Especialidad: ")

                entrenador = registrar_entrenador(
                    nombre,
                    especialidad
                )

                print(
                    f"  ✓ Entrenador registrado con ID "
                    f"{entrenador.id_entrenador}."
                )

            elif opcion == 2:
                entrenadores = listar_entrenadores()

                if not entrenadores:
                    print("  Sin entrenadores registrados.")
                else:
                    separador("Lista de entrenadores")

                    for e in entrenadores:
                        print(
                            f"  [{e.id_entrenador}] "
                            f"{e.nombre} — {e.especialidad}"
                        )

            elif opcion == 3:

                id_entrenador = int(
                    input("  ID del entrenador: ")
                )

                nombre = input(
                    "  Nuevo nombre: "
                )

                especialidad = input(
                    "  Nueva especialidad: "
                )

                entrenador = actualizar_entrenador(
                    id_entrenador,
                    nombre,
                    especialidad
                )

                print(
                    f"  ✓ Actualizado: "
                    f"{entrenador.nombre}"
                )

            elif opcion == 4:

                id_entrenador = int(
                    input("  ID del entrenador: ")
                )

                eliminar_entrenador(
                    id_entrenador
                )

                print(
                    "  ✓ Entrenador eliminado."
                )

            elif opcion == 0:
                break

            else:
                print("  Opción inválida.")

        except ValueError:
            print(
                "  Error de valor. "
                "Ingrese una opción válida"
            )

        except Exception as e:
            print(
                f"  Error inesperado: {e}"
            )

        pausar()

# ─────────────────────────────────────────────
#  MÓDULO: OPERACIONES
# ─────────────────────────────────────────────

def menu_operaciones():
    while True:
        separador("OPERACIONES")
        print("  1. Inscribir miembro en clase")
        print("  2. Registrar asistencia")
        print("  3. Listar inscripciones")
        print("  4. Listar asistencias")
        print("  0. ← Volver")

        try:
            opcion = int(input("\n  Opción: "))

            if opcion == 1:
                id_miembro = int(input("  ID del miembro: "))
                id_clase   = int(input("  ID de la clase: "))
                print(f"  {inscribir_miembro(id_miembro, id_clase)}")

            elif opcion == 2:
                id_miembro = int(input("  ID del miembro: "))
                id_clase   = int(input("  ID de la clase: "))
                print(f"  {registrar_asistencia(id_miembro, id_clase)}")


            elif opcion == 3:
                inscripciones = listar_inscripciones()
                if not inscripciones:
                    print("  Sin inscripciones registradas.")
                else:
                    separador("Lista de inscripciones")
                    for idx, i in enumerate(inscripciones, start=1):
                        print(f"  [{idx}] Miembro {i['id_miembro']} → Clase {i['id_clase']}")

            elif opcion == 4:
                asistencias = listar_asistencias()
                if not asistencias:
                    print("  Sin asistencias registradas.")
                else:
                    separador("Lista de asistencias")
                    for idx, i in enumerate(asistencias, start=1):
                        print(f"[{idx}] Miembro {i['id_miembro']} -> Clase: {i['id_clase']} Fecha y Hora: {i['fecha_hora']}")
            elif opcion == 0:
                break
            else:
                print("  Opción inválida.")

        except ValueError as e:
            print(f"  Error de valor. Ingrese una opcion valida")
        except Exception as e:
            print(f"  Error inesperado: {e}")

        pausar()


# ─────────────────────────────────────────────
#  MENÚ PRINCIPAL
# ─────────────────────────────────────────────

def menu_principal():
    while True:
        print("\n╔══════════════════════════════════════╗")
        print("║        SISTEMA DE GIMNASIO           ║")
        print("╠══════════════════════════════════════╣")
        print("║  1.  👤  Miembros                    ║")
        print("║  2.  🏋️   Clases                     ║")
        print("║  3.  🧑‍🏫  Entrenadores                ║")
        print("║  4.  📋  Operaciones                 ║")
        print("║  0.  🚪  Salir                       ║")
        print("╚══════════════════════════════════════╝")

        try:
            opcion = int(input("\n  Módulo: "))

            if opcion == 1:
                menu_miembros()
            elif opcion == 2:
                menu_clases()
            elif opcion == 3:
                menu_entrenadores()
            elif opcion == 4:
                menu_operaciones()
            elif opcion == 0:
                print("\n  Hasta luego.\n")
                break
            else:
                print("  Opción inválida.")

        except ValueError as e:
            print(f"  Error de valor. Ingrese una opcion valida")
        except Exception as e:
            print(f"  Error inesperado: {e}")


if __name__ == "__main__":
    menu_principal()