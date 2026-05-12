class Miembro:
    def __init__(self, id_miembro, nombre, apellido, email):
        self.id_miembro = id_miembro
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def a_diccionario(self):
        return {
            "id_miembro": self.id_miembro,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email
        }