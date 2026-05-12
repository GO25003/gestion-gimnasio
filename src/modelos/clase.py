class Clase:
    def __init__(self, id_clase, nombre_disciplina, horario, capacidad_maxima):
        self.id_clase = id_clase
        self.nombre_disciplina = nombre_disciplina
        self.horario = horario
        self.capacidad_maxima = capacidad_maxima

    def a_diccionario(self):
        return {
            "id_clase": self.id_clase,
            "nombre_disciplina": self.nombre_disciplina,
            "horario": self.horario,
            "capacidad_maxima": self.capacidad_maxima
        }