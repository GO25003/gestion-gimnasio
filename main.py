from servicios.servicio_miembros import registrar_miembro, listar_miembros
from servicios.servicio_clases import listar_clases
from servicios.servicio_inscripciones import inscribir_miembro
from servicios.servicio_asistencias import registrar_asistencia


def mostrar_menu():
    print("\n===== SISTEMA GIMNASIO =====")
    print("1. Registrar miembro")
    print("2. Listar miembros")
    print("3. Listar clases")
    print("4. Inscribir miembro en clase")
    print("5. Registrar asistencia")
    print("6. Salir")


def main():
    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                email = input("Email: ")

                miembro = registrar_miembro(nombre, apellido, email)
                print(f"Miembro registrado con ID {miembro.id_miembro}")

            elif opcion == 2:
                miembros = listar_miembros()
                if not miembros:
                    print("No hay miembros registrados.")
                else:
                    for m in miembros:
                        print(f"ID: {m.id_miembro} | {m.nombre} {m.apellido} | {m.email}")

            elif opcion == 3:
                clases = listar_clases()
                if not clases:
                    print("No hay clases registradas.")
                else:
                    for c in clases:
                        print(f"ID: {c.id_clase} | {c.nombre_disciplina} | Horario: {c.horario} | Cupo: {c.capacidad_maxima}")

            elif opcion == 4:
                id_miembro = int(input("ID del miembro: "))
                id_clase = int(input("ID de la clase: "))

                inscribir_miembro(id_miembro, id_clase)
                print("Inscripción realizada correctamente.")

            elif opcion == 5:
                id_miembro = int(input("ID del miembro: "))
                id_clase = int(input("ID de la clase: "))

                registrar_asistencia(id_miembro, id_clase)
                print("Asistencia registrada correctamente.")

            elif opcion == 6:
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()