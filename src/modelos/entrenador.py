class Entrenador:
    def __init__(self, id_entrenador, nombre, especialidad):
        self.id_entrenador = id_entrenador
        self.nombre = nombre
        self.especialidad = especialidad

    def a_diccionario(self):
        return {
            "id_entrenador": self.id_entrenador,
            "nombre": self.nombre,
            "especialidad": self.especialidad
        }