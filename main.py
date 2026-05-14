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
from servicios.servicio_inscripciones import inscribir_miembro
from servicios.servicio_asistencias import registrar_asistencia


def mostrar_menu():
    print("\n===== SISTEMA GIMNASIO =====")
    print("--- MIEMBROS ---")
    print("1. Registrar miembro")
    print("2. Listar miembros")
    print("3. Buscar miembro por ID")
    print("4. Actualizar miembro")
    print("5. Eliminar miembro")
    print("--- CLASES ---")
    print("6. Crear clase")
    print("7. Listar clases")
    print("8. Buscar clase por ID")
    print("9. Actualizar clase")
    print("10. Eliminar clase")
    print("--- OTROS ---")
    print("11. Inscribir miembro en clase")
    print("12. Registrar asistencia")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()

        try:
            opcion = int(input("\nSeleccione una opción: "))

            # ── MIEMBROS ──────────────────────────────────────────
            if opcion == 1:
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                email = input("Email: ")
                miembro = registrar_miembro(nombre, apellido, email)
                print(f"✓ Miembro registrado con ID {miembro.id_miembro}.")

            elif opcion == 2:
                miembros = listar_miembros()
                if not miembros:
                    print("No hay miembros registrados.")
                else:
                    for m in miembros:
                        print(f"ID: {m.id_miembro} | {m.nombre} {m.apellido} | {m.email}")

            elif opcion == 3:
                id_miembro = int(input("ID del miembro: "))
                miembro = buscar_miembro_por_id(id_miembro)
                if miembro:
                    print(f"ID: {miembro.id_miembro} | {miembro.nombre} {miembro.apellido} | {miembro.email}")
                else:
                    print("Miembro no encontrado.")

            elif opcion == 4:
                id_miembro = int(input("ID del miembro a actualizar: "))
                miembro = buscar_miembro_por_id(id_miembro)
                if not miembro:
                    print("Miembro no encontrado.")
                else:
                    print(f"Datos actuales: {miembro.nombre} {miembro.apellido} | {miembro.email}")
                    print("(Deja en blanco para no cambiar ese campo)")
                    nuevo_nombre = input("Nuevo nombre: ")
                    nuevo_apellido = input("Nuevo apellido: ")
                    nuevo_email = input("Nuevo email: ")
                    actualizado = actualizar_miembro(
                        id_miembro,
                        nuevo_nombre or None,
                        nuevo_apellido or None,
                        nuevo_email or None
                    )
                    print(f"✓ Miembro actualizado: {actualizado.nombre} {actualizado.apellido} | {actualizado.email}")

            elif opcion == 5:
                id_miembro = int(input("ID del miembro a eliminar: "))
                if eliminar_miembro(id_miembro):
                    print("✓ Miembro eliminado correctamente.")
                else:
                    print("Miembro no encontrado.")

            # ── CLASES ────────────────────────────────────────────
            elif opcion == 6:
                nombre = input("Nombre de la disciplina: ")
                horario = input("Horario (ej: Lunes 08:00): ")
                capacidad = int(input("Capacidad máxima: "))
                clase = crear_clase(nombre, horario, capacidad)
                print(f"✓ Clase creada con ID {clase.id_clase}.")

            elif opcion == 7:
                clases = listar_clases()
                if not clases:
                    print("No hay clases registradas.")
                else:
                    for c in clases:
                        print(f"ID: {c.id_clase} | {c.nombre_disciplina} | {c.horario} | Cupo: {c.capacidad_maxima}")

            elif opcion == 8:
                id_clase = int(input("ID de la clase: "))
                clase = buscar_clase_por_id(id_clase)
                if clase:
                    print(f"ID: {clase.id_clase} | {clase.nombre_disciplina} | {clase.horario} | Cupo: {clase.capacidad_maxima}")
                else:
                    print("Clase no encontrada.")

            elif opcion == 9:
                id_clase = int(input("ID de la clase a actualizar: "))
                clase = buscar_clase_por_id(id_clase)
                if not clase:
                    print("Clase no encontrada.")
                else:
                    print(f"Datos actuales: {clase.nombre_disciplina} | {clase.horario} | Cupo: {clase.capacidad_maxima}")
                    print("(Deja en blanco para no cambiar ese campo)")
                    nuevo_nombre = input("Nuevo nombre de disciplina: ")
                    nuevo_horario = input("Nuevo horario: ")
                    nueva_capacidad_str = input("Nueva capacidad: ")
                    nueva_capacidad = int(nueva_capacidad_str) if nueva_capacidad_str.strip() else None
                    actualizada = actualizar_clase(
                        id_clase,
                        nuevo_nombre or None,
                        nuevo_horario or None,
                        nueva_capacidad
                    )
                    print(f"✓ Clase actualizada: {actualizada.nombre_disciplina} | {actualizada.horario} | Cupo: {actualizada.capacidad_maxima}")

            elif opcion == 10:
                id_clase = int(input("ID de la clase a eliminar: "))
                if eliminar_clase(id_clase):
                    print("✓ Clase eliminada correctamente.")
                else:
                    print("Clase no encontrada.")

            # ── OTROS ─────────────────────────────────────────────
            elif opcion == 11:
                id_miembro = int(input("ID del miembro: "))
                id_clase = int(input("ID de la clase: "))
                resultado = inscribir_miembro(id_miembro, id_clase)
                print(resultado)

            elif opcion == 12:
                id_miembro = int(input("ID del miembro: "))
                id_clase = int(input("ID de la clase: "))
                resultado = registrar_asistencia(id_miembro, id_clase)
                print(resultado)

            elif opcion == 0:
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except ValueError as e:
            print(f"Error de valor: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()