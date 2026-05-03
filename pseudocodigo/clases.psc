Algoritmo clases
    Definir opcion Como Entero
    Definir id1, nombre1, horario1, entrenador1 Como Cadena
    Definir cupo1, inscritos1 Como Entero
    Definir id2, nombre2, horario2, entrenador2 Como Cadena
    Definir cupo2, inscritos2 Como Entero
    Definir id3, nombre3, horario3, entrenador3 Como Cadena
    Definir cupo3, inscritos3 Como Entero
    Definir id_buscar Como Cadena
    
    // Inicializar vacíos
    id1 <- ""
    nombre1 <- ""
    horario1 <- ""
    entrenador1 <- ""
    cupo1 <- 0
    inscritos1 <- 0
    
    id2 <- ""
    nombre2 <- ""
    horario2 <- ""
    entrenador2 <- ""
    cupo2 <- 0
    inscritos2 <- 0
    
    id3 <- ""
    nombre3 <- ""
    horario3 <- ""
    entrenador3 <- ""
    cupo3 <- 0
    inscritos3 <- 0
    
    Repetir
        Escribir ""
        Escribir "CLASES"
        Escribir "1. Crear clase"
        Escribir "2. Buscar clase"
        Escribir "3. Actualizar clase"
        Escribir "4. Eliminar clase"
        Escribir "5. Ver cupo disponible"
        Escribir "6. Inscribir miembro"
        Escribir "7. Salir"
        Leer opcion
        
        // Opcion 1: Crear clase
        Si opcion = 1 Entonces
            Escribir "CREAR CLASE"
            Si id1 = "" Entonces
                Escribir "ID de la clase:"
                Leer id1
                Escribir "Nombre:"
                Leer nombre1
                Escribir "Horario:"
                Leer horario1
                Escribir "Cupo maximo:"
                Leer cupo1
                Escribir "ID del entrenador:"
                Leer entrenador1
                inscritos1 <- 0
                Escribir "Clase guardada"
            Sino
                Si id2 = "" Entonces
                    Escribir "ID de la clase:"
                    Leer id2
                    Escribir "Nombre:"
                    Leer nombre2
                    Escribir "Horario:"
                    Leer horario2
                    Escribir "Cupo maximo:"
                    Leer cupo2
                    Escribir "ID del entrenador:"
                    Leer entrenador2
                    inscritos2 <- 0
                    Escribir "Clase guardada"
                Sino
                    Si id3 = "" Entonces
                        Escribir "ID de la clase:"
                        Leer id3
                        Escribir "Nombre:"
                        Leer nombre3
                        Escribir "Horario:"
                        Leer horario3
                        Escribir "Cupo maximo:"
                        Leer cupo3
                        Escribir "ID del entrenador:"
                        Leer entrenador3
                        inscritos3 <- 0
                        Escribir "Clase guardada"
                    Sino
                        Escribir "No hay espacio (maximo 3 clases)"
                    FinSi
                FinSi
            FinSi
        FinSi
        
        // Opcion 2: Buscar clase
        Si opcion = 2 Entonces
            Escribir "BUSCAR CLASE"
            Escribir "ID de la clase:"
            Leer id_buscar
            Si id1 = id_buscar Entonces
                Escribir "ID: ", id1
                Escribir "Nombre: ", nombre1
                Escribir "Horario: ", horario1
                Escribir "Cupo: ", inscritos1, "/", cupo1
                Escribir "Entrenador ID: ", entrenador1
            Sino
                Si id2 = id_buscar Entonces
                    Escribir "ID: ", id2
                    Escribir "Nombre: ", nombre2
                    Escribir "Horario: ", horario2
                    Escribir "Cupo: ", inscritos2, "/", cupo2
                    Escribir "Entrenador ID: ", entrenador2
                Sino
                    Si id3 = id_buscar Entonces
                        Escribir "ID: ", id3
                        Escribir "Nombre: ", nombre3
                        Escribir "Horario: ", horario3
                        Escribir "Cupo: ", inscritos3, "/", cupo3
                        Escribir "Entrenador ID: ", entrenador3
                    Sino
                        Escribir "No se encontro la clase"
                    FinSi
                FinSi
            FinSi
        FinSi
        
        // Opcion 3: Actualizar clase
        Si opcion = 3 Entonces
            Escribir "ACTUALIZAR CLASE"
            Escribir "ID de la clase a actualizar:"
            Leer id_buscar
            Si id1 = id_buscar Entonces
                Escribir "Nuevo nombre:"
                Leer nombre1
                Escribir "Nuevo horario:"
                Leer horario1
                Escribir "Nuevo cupo maximo:"
                Leer cupo1
                Si cupo1 < inscritos1 Entonces
                    Escribir "Error: El cupo no puede ser menor a los inscritos (", inscritos1, ")"
                    cupo1 <- inscritos1
                FinSi
                Escribir "Nuevo ID de entrenador:"
                Leer entrenador1
                Escribir "Clase actualizada"
            Sino
                Si id2 = id_buscar Entonces
                    Escribir "Nuevo nombre:"
                    Leer nombre2
                    Escribir "Nuevo horario:"
                    Leer horario2
                    Escribir "Nuevo cupo maximo:"
                    Leer cupo2
                    Si cupo2 < inscritos2 Entonces
                        Escribir "Error: El cupo no puede ser menor a los inscritos (", inscritos2, ")"
                        cupo2 <- inscritos2
                    FinSi
                    Escribir "Nuevo ID de entrenador:"
                    Leer entrenador2
                    Escribir "Clase actualizada"
                Sino
                    Si id3 = id_buscar Entonces
                        Escribir "Nuevo nombre:"
                        Leer nombre3
                        Escribir "Nuevo horario:"
                        Leer horario3
                        Escribir "Nuevo cupo maximo:"
                        Leer cupo3
                        Si cupo3 < inscritos3 Entonces
                            Escribir "Error: El cupo no puede ser menor a los inscritos (", inscritos3, ")"
                            cupo3 <- inscritos3
                        FinSi
                        Escribir "Nuevo ID de entrenador:"
                        Leer entrenador3
                        Escribir "Clase actualizada"
                    Sino
                        Escribir "No se encontro la clase"
                    FinSi
                FinSi
            FinSi
        FinSi
        
        // Opcion 4: Eliminar clase
        Si opcion = 4 Entonces
            Escribir "ELIMINAR CLASE"
            Escribir "ID de la clase a eliminar:"
            Leer id_buscar
            Si id1 = id_buscar Entonces
                id1 <- ""
                nombre1 <- ""
                horario1 <- ""
                cupo1 <- 0
                inscritos1 <- 0
                entrenador1 <- ""
                Escribir "Clase eliminada"
            Sino
                Si id2 = id_buscar Entonces
                    id2 <- ""
                    nombre2 <- ""
                    horario2 <- ""
                    cupo2 <- 0
                    inscritos2 <- 0
                    entrenador2 <- ""
                    Escribir "Clase eliminada"
                Sino
                    Si id3 = id_buscar Entonces
                        id3 <- ""
                        nombre3 <- ""
                        horario3 <- ""
                        cupo3 <- 0
                        inscritos3 <- 0
                        entrenador3 <- ""
                        Escribir "Clase eliminada"
                    Sino
                        Escribir "No se encontro la clase"
                    FinSi
                FinSi
            FinSi
        FinSi
        
        // Opcion 5: Ver cupo disponible
        Si opcion = 5 Entonces
            Escribir "VER CUPO"
            Escribir "ID de la clase:"
            Leer id_buscar
            Si id1 = id_buscar Entonces
                Escribir "Cupos disponibles: ", cupo1 - inscritos1
            Sino
                Si id2 = id_buscar Entonces
                    Escribir "Cupos disponibles: ", cupo2 - inscritos2
                Sino
                    Si id3 = id_buscar Entonces
                        Escribir "Cupos disponibles: ", cupo3 - inscritos3
                    Sino
                        Escribir "No se encontro la clase"
                    FinSi
                FinSi
            FinSi
        FinSi
        
        // Opcion 6: Inscribir miembro
        Si opcion = 6 Entonces
            Escribir "INSCRIBIR MIEMBRO"
            Escribir "ID de la clase:"
            Leer id_buscar
            Si id1 = id_buscar Entonces
                Si inscritos1 < cupo1 Entonces
                    inscritos1 <- inscritos1 + 1
                    Escribir "Miembro inscrito. Cupos ocupados: ", inscritos1, "/", cupo1
                Sino
                    Escribir "Error: Clase llena"
                FinSi
            Sino
                Si id2 = id_buscar Entonces
                    Si inscritos2 < cupo2 Entonces
                        inscritos2 <- inscritos2 + 1
                        Escribir "Miembro inscrito. Cupos ocupados: ", inscritos2, "/", cupo2
                    Sino
                        Escribir "Error: Clase llena"
                    FinSi
                Sino
                    Si id3 = id_buscar Entonces
                        Si inscritos3 < cupo3 Entonces
                            inscritos3 <- inscritos3 + 1
                            Escribir "Miembro inscrito. Cupos ocupados: ", inscritos3, "/", cupo3
                        Sino
                            Escribir "Error: Clase llena"
                        FinSi
                    Sino
                        Escribir "No se encontro la clase"
                    FinSi
                FinSi
            FinSi
        FinSi
        
    Hasta Que opcion = 7
    
FinAlgoritmo