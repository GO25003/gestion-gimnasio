Algoritmo Inscripciones
	
	Definir maxInscripciones, numInscripciones, opcion Como Entero
	
	maxInscripciones <- 100
	numInscripciones <- 0
	
	// Definimos tipos antes de dimensionar para evitar conflictos
	Definir idMiembro, idClase Como Entero
	Definir fechaInscripcion Como Cadena
	
	Dimension idMiembro[100]
	Dimension idClase[100]
	Dimension fechaInscripcion[100]
	
	Repetir
		Limpiar Pantalla
		Escribir "===== MODULO INSCRIPCIONES ====="
		Escribir "1. Inscribir miembro a clase"
		Escribir "2. Ver inscripciones"
		Escribir "3. Eliminar inscripcion"
		Escribir "4. Salir"
		Escribir "Seleccione una opcion: "
		Leer opcion
		
		Segun opcion Hacer
			1:
				InscribirMiembro(numInscripciones, idMiembro, idClase, fechaInscripcion, maxInscripciones)
			2:
				VerInscripciones(idMiembro, idClase, fechaInscripcion, numInscripciones)
			3:
				EliminarInscripcion(numInscripciones, idMiembro, idClase, fechaInscripcion)
			4:
				Escribir "Saliendo..."
			De Otro Modo:
				Escribir "Opcion invalida"
		FinSegun
		
		Si opcion <> 4 Entonces
			Escribir "Presione una tecla para continuar..."
			Esperar Tecla
		FinSi
		
	Hasta Que opcion = 4
	
FinAlgoritmo

SubProceso InscribirMiembro(numInscripciones Por Referencia, idMiembro, idClase, fechaInscripcion, maxInscripciones)
	Definir idM, idC, i Como Entero
	Definir fecha Como Cadena
	Definir inscripcionExiste Como Logico
	
	Limpiar Pantalla
	Escribir "===== INSCRIBIR MIEMBRO A CLASE ====="
	
	Si numInscripciones >= maxInscripciones Entonces
		Escribir "No hay espacio para mas inscripciones"
	Sino
		Escribir "Ingrese ID del miembro: "
		Leer idM
		Escribir "Ingrese ID de la clase: "
		Leer idC
		Escribir "Ingrese fecha (DD/MM/YYYY): "
		Leer fecha
		
		inscripcionExiste <- Falso
		i <- 1
		// Usamos Mientras para evitar errores si numInscripciones es 0
		Mientras i <= numInscripciones Y inscripcionExiste = Falso Hacer
			Si idMiembro[i] = idM Y idClase[i] = idC Entonces
				inscripcionExiste <- Verdadero
			FinSi
			i <- i + 1
		FinMientras
		
		Si inscripcionExiste Entonces
			Escribir "Error: El miembro ya esta en esa clase."
		Sino
			numInscripciones <- numInscripciones + 1
			idMiembro[numInscripciones] <- idM
			idClase[numInscripciones] <- idC
			fechaInscripcion[numInscripciones] <- fecha
			Escribir "Inscripcion registrada exitosamente."
		FinSi
	FinSi
FinSubProceso

SubProceso VerInscripciones(idMiembro, idClase, fechaInscripcion, numInscripciones)
	Definir i Como Entero
	Limpiar Pantalla
	Escribir "===== INSCRIPCIONES REGISTRADAS ====="
	Si numInscripciones = 0 Entonces
		Escribir "No hay inscripciones registradas."
	Sino
		// Ciclo seguro: solo entra si numInscripciones > 0
		Para i <- 1 Hasta numInscripciones Hacer
			Escribir i, ". ID Miembro: ", idMiembro[i], " | ID Clase: ", idClase[i], " | Fecha: ", fechaInscripcion[i]
		FinPara
		Escribir ""
		Escribir "Total: ", numInscripciones
	FinSi
FinSubProceso

SubProceso EliminarInscripcion(numInscripciones Por Referencia, idMiembro, idClase, fechaInscripcion)
	Definir idM, idC, i, j Como Entero
	Definir encontrado Como Logico
	
	Limpiar Pantalla
	Escribir "===== ELIMINAR INSCRIPCION ====="
	
	Si numInscripciones = 0 Entonces
		Escribir "No hay nada que eliminar."
	Sino
		Escribir "Ingrese ID del miembro: "
		Leer idM
		Escribir "Ingrese ID de la clase: "
		Leer idC
		
		encontrado <- Falso
		i <- 1
		
		// Buscamos el elemento
		Mientras i <= numInscripciones Y encontrado = Falso Hacer
			Si idMiembro[i] = idM Y idClase[i] = idC Entonces
				encontrado <- Verdadero
				
				// Desplazamos los elementos siguientes hacia la izquierda
				j <- i
				Mientras j < numInscripciones Hacer
					idMiembro[j] <- idMiembro[j + 1]
					idClase[j] <- idClase[j + 1]
					fechaInscripcion[j] <- fechaInscripcion[j + 1]
					j <- j + 1
				FinMientras
				
				numInscripciones <- numInscripciones - 1
				Escribir "Inscripcion eliminada correctamente."
			Sino
				i <- i + 1
			FinSi
		FinMientras
		
		Si encontrado = Falso Entonces
			Escribir "No se encontro ninguna inscripcion con esos datos."
		FinSi
	FinSi
FinSubProceso