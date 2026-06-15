import unittest

from src.servicios.servicio_clases import (
    crear_clase
)

from src.servicios.servicio_entrenadores import (
    registrar_entrenador
)


class TestServicioClases(unittest.TestCase):

    def test_crear_clase(self):

        registrar_entrenador(
            "Laura",
            "Yoga"
        )

        clase = crear_clase(
            "Yoga",
            "Lunes 08:00",
            20,
            "Laura"
        )

        self.assertEqual(
            clase.nombre_disciplina,
            "Yoga"
        )

        self.assertEqual(
            clase.entrenador,
            "Laura"
        )


if __name__ == "__main__":
    unittest.main()