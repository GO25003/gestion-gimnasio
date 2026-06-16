# Gestion Gimnasio

Aplicación CLI en Python para la gestión de un gimnasio. Permite administrar miembros, entrenadores, clases e inscripciones con control de cupo y detección de choques de horario.

---

## Integrantes

* **Johanna Annelisse Lopez Escobar** - LE25007  
* **Diego Elias Fuentes Alfaro** - FA23009  
* **Carlos Ernesto Garcia Ocampo** - GO25003

---

## Avance #1 (14/04/2026) - Lógica en PSeInt

Se ha definido la lógica y los flujos de control utilizando pseudocódigo como base antes de la implementación en Python.

### Funcionalidades desarrolladas:

* **`clases.psc`**: Creación de clases con gestión de horario, cupo máximo y asignación de entrenador.
* **`entrenadores.psc`**: CRUD completo (Registrar, buscar, actualizar y eliminar) de entrenadores.
* **`inscripciones.psc`**: Gestión de inscripciones de miembros con validación automática de cupo.

## Avance #2 (19/5/2026) — Implementación en Python  


En esta etapa se inició la implementación funcional del sistema en Python, utilizando programación orientada a objetos, persistencia de datos con archivos JSON y una arquitectura dividida en modelos, servicios y repositorios.

## Funcionalidades implementadas

### Gestión de clases
- Creación de clases de gimnasio.
- Validación de capacidad máxima.
- Generación automática de ID.
- Persistencia en `clases.json`.

### Gestión de entrenadores
- Registro y listado de entrenadores.
- Validación de datos.
- Persistencia en `entrenadores.json`.

### Gestión de miembros
- Registro y búsqueda de miembros.
- Validación de información.
- Persistencia en `miembros.json`.

### Gestión de inscripciones
- Validación de existencia de miembros y clases.
- Verificación de cupos disponibles.
- Persistencia en `inscripciones.json`.

### Gestión de asistencias
- Registro automático de fecha y hora usando `datetime`.
- Validación de inscripción previa del miembro.
- Persistencia en `asistencias.json`.

### Interfaz CLI
- Implementación de menú principal interactivo.
- Manejo de errores con `try/except`.


## Avance #3 (19/5/2026) — Entrega final

Para esta entrega final, se han mejorado los mensajes de error para mostrarle algo mas amigable al usuario, se completo el CRUD de entrenadores, y se implementaron pruebas unitarias 
### Pruebas unitarias
- Pruebas unitarias para asistencias, inscripciones, clases y entrenadores

### Manejo de errores
- Se implemento un mensaje mas amigable para el usuario para cuando se capta un error

### CRUD entrenadores
- Se completo el CRUD de entrenadores y se agregar una validacion en las clases, verificando que el entrenador exista al momento de crear una clase

---
## Tecnologías utilizadas

- Python 3
- JSON

## Ejecución del proyecto

## Clonar el repositorio

### HTTPS

```bash
git clone https://github.com/GO25003/gestion-gimnasio.git
```

### SSH

```bash
git clone git@github.com:GO25003/gestion-gimnasio.git
```

### Ejecutar el sistema

```bash
python main.py
```

### Requisitos

- Python 3 instalado

    
