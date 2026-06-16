import unittest

from src.servicios.servicio_entrenadores import (
    registrar_entrenador
)


class TestServicioEntrenadores(unittest.TestCase):

    def test_registrar_entrenador(self):
        entrenador = registrar_entrenador(
            "Pedro",
            "Crossfit"
        )

        self.assertEqual(
            entrenador.nombre,
            "Pedro"
        )

        self.assertEqual(
            entrenador.especialidad,
            "Crossfit"
        )


if __name__ == "__main__":
    unittest.main()