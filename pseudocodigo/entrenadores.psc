Algoritmo entrenadores
    Definir opcion Como Entero
    Definir id1, nombre1, espe1 Como Cadena
    Definir id2, nombre2, espe2 Como Cadena
    Definir id3, nombre3, espe3 Como Cadena
    Definir id_buscar Como Cadena
    
    // Inicializar vacíos
    id1 <- ""
    nombre1 <- ""
    espe1 <- ""
    id2 <- ""
    nombre2 <- ""
    espe2 <- ""
    id3 <- ""
    nombre3 <- ""
    espe3 <- ""
    
    Repetir
        Escribir ""
        Escribir "ENTRENADORES"
        Escribir "1. Registrar"
        Escribir "2. Buscar"
        Escribir "3. Actualizar"
        Escribir "4. Eliminar"
        Escribir "5. Salir"
        Leer opcion
        
        // Opcion 1: Registrar
        Si opcion = 1 Entonces
            Escribir "--- REGISTRAR ---"
            Si id1 = "" Entonces
                Escribir "ID:"
                Leer id1
                Escribir "Nombre:"
                Leer nombre1
                Escribir "Especialidad:"
                Leer espe1
                Escribir "Entrenador guardado"
            Sino
                Si id2 = "" Entonces
                    Escribir "ID:"
                    Leer id2
                    Escribir "Nombre:"
                    Leer nombre2
                    Escribir "Especialidad:"
                    Leer espe2
                    Escribir "Entrenador guardado"
                Sino
                    Si id3 = "" Entonces
                        Escribir "ID:"
                        Leer id3
                        Escribir "Nombre:"
                        Leer nombre3
                        Escribir "Especialidad:"
                        Leer espe3
                        Escribir "Entrenador guardado"
                    Sino
                        Escribir "No hay espacio (maximo 3 entrenadores)"
                    FinSi
                FinSi
            FinSi
        FinSi
        
        // Opcion 2: Buscar
        Si opcion = 2 Entonces
            Escribir "--- BUSCAR ---"
            Escribir "ID a buscar:"
            Leer id_buscar
            Si id1 = id_buscar Entonces
                Escribir "ID: ", id1
                Escribir "Nombre: ", nombre1
                Escribir "Especialidad: ", espe1
            Sino
                Si id2 = id_buscar Entonces
                    Escribir "ID: ", id2
                    Escribir "Nombre: ", nombre2
                    Escribir "Especialidad: ", espe2
                Sino
                    Si id3 = id_buscar Entonces
                        Escribir "ID: ", id3
                        Escribir "Nombre: ", nombre3
                        Escribir "Especialidad: ", espe3
                    Sino
                        Escribir "No se encontro el entrenador"
                    FinSi
                FinSi
            FinSi
        FinSi
        
        // Opcion 3: Actualizar
        Si opcion = 3 Entonces
            Escribir "--- ACTUALIZAR ---"
            Escribir "ID del entrenador a actualizar:"
            Leer id_buscar
            Si id1 = id_buscar Entonces
                Escribir "Nuevo nombre:"
                Leer nombre1
                Escribir "Nueva especialidad:"
                Leer espe1
                Escribir "Entrenador actualizado"
            Sino
                Si id2 = id_buscar Entonces
                    Escribir "Nuevo nombre:"
                    Leer nombre2
                    Escribir "Nueva especialidad:"
                    Leer espe2
                    Escribir "Entrenador actualizado"
                Sino
                    Si id3 = id_buscar Entonces
                        Escribir "Nuevo nombre:"
                        Leer nombre3
                        Escribir "Nueva especialidad:"
                        Leer espe3
                        Escribir "Entrenador actualizado"
                    Sino
                        Escribir "No se encontro el entrenador"
                    FinSi
                FinSi
            FinSi
        FinSi
        
        // Opcion 4: Eliminar
        Si opcion = 4 Entonces
            Escribir "--- ELIMINAR ---"
            Escribir "ID del entrenador a eliminar:"
            Leer id_buscar
            Si id1 = id_buscar Entonces
                id1 <- ""
                nombre1 <- ""
                espe1 <- ""
                Escribir "Entrenador eliminado"
            Sino
                Si id2 = id_buscar Entonces
                    id2 <- ""
                    nombre2 <- ""
                    espe2 <- ""
                    Escribir "Entrenador eliminado"
                Sino
                    Si id3 = id_buscar Entonces
                        id3 <- ""
                        nombre3 <- ""
                        espe3 <- ""
                        Escribir "Entrenador eliminado"
                    Sino
                        Escribir "No se encontro el entrenador"
                    FinSi
                FinSi
            FinSi
        FinSi
        
    Hasta Que opcion = 5
    
    Escribir "Programa finalizado"
FinAlgoritmo
