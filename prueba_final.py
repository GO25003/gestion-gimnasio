import sys
import os

# Agregar la carpeta 'src' al path para poder importar los servicios
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from servicios.servicio_clases import crear_clase, listar_clases
from servicios.servicio_entrenadores import registrar_entrenador, listar_entrenadores

print("=== PRUEBA DE MÓDULOS JOHANA ===\n")

# Probar crear clase
print("1. Creando clase 'Yoga'...")
clase1 = crear_clase("Yoga", "Lunes 10am", 15)
print(f"   ✓ Clase creada con ID: {clase1.id_clase}")

# Probar listar clases
print("\n2. Listando clases:")
for c in listar_clases():
    print(f"   ID:{c.id_clase} | {c.nombre_disciplina} | {c.horario} | Cupo:{c.capacidad_maxima}")

# Probar registrar entrenador
print("\n3. Registrando entrenador 'Ana'...")
entrenador1 = registrar_entrenador("Ana", "Yoga")
print(f"   ✓ Entrenador registrado con ID: {entrenador1.id_entrenador}")

# Probar listar entrenadores
print("\n4. Listando entrenadores:")
for e in listar_entrenadores():
    print(f"   ID:{e.id_entrenador} | {e.nombre} | Especialidad:{e.especialidad}")

print("\n✅ Prueba exitosa. Los JSON se han creado en la carpeta 'datos'.")