import sys
import os

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "src"
    )
)

from unittest.mock import patch
from servicios.servicio_asistencias import (
    registrar_asistencia,
    listar_asistencias
)


@patch("servicios.servicio_asistencias.guardar_asistencias")
@patch("servicios.servicio_asistencias.cargar_asistencias")
@patch("servicios.servicio_asistencias.cargar_inscripciones")
def test_registrar_asistencia_exitosa(
    mock_cargar_inscripciones,
    mock_cargar_asistencias,
    mock_guardar_asistencias
):
    mock_cargar_inscripciones.return_value = [
        {
            "id_miembro": 1,
            "id_clase": 101
        }
    ]

    mock_cargar_asistencias.return_value = []

    resultado = registrar_asistencia(1, 101)

    assert resultado == "Asistencia registrada correctamente."

    mock_guardar_asistencias.assert_called_once()

    asistencias_guardadas = (
        mock_guardar_asistencias.call_args[0][0]
    )

    assert len(asistencias_guardadas) == 1
    assert asistencias_guardadas[0]["id_miembro"] == 1
    assert asistencias_guardadas[0]["id_clase"] == 101


@patch("servicios.servicio_asistencias.cargar_inscripciones")
def test_registrar_asistencia_sin_inscripcion(
    mock_cargar_inscripciones
):
    mock_cargar_inscripciones.return_value = []

    resultado = registrar_asistencia(1, 101)

    assert resultado == (
        "El miembro no está inscrito en esta clase."
    )


@patch("servicios.servicio_asistencias.cargar_asistencias")
def test_listar_asistencias(
    mock_cargar_asistencias
):
    datos = [
        {
            "id_miembro": 1,
            "id_clase": 101,
            "fecha_hora": "2026-01-01 10:00:00"
        }
    ]

    mock_cargar_asistencias.return_value = datos

    assert listar_asistencias() == datos



import sys
import os

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "src"
    )
)

from datos import repositorio_asistencias


def test_cargar_asistencias_archivo_inexistente(
    monkeypatch,
    tmp_path
):
    ruta = tmp_path / "asistencias.json"

    monkeypatch.setattr(
        repositorio_asistencias,
        "RUTA",
        str(ruta)
    )

    resultado = repositorio_asistencias.cargar_asistencias()

    assert resultado == []


def test_guardar_y_cargar_asistencias(
    monkeypatch,
    tmp_path
):
    ruta = tmp_path / "asistencias.json"

    monkeypatch.setattr(
        repositorio_asistencias,
        "RUTA",
        str(ruta)
    )

    datos = [
        {
            "id_miembro": 1,
            "id_clase": 101,
            "fecha_hora": "2026-01-01 10:00:00"
        }
    ]

    repositorio_asistencias.guardar_asistencias(datos)

    resultado = repositorio_asistencias.cargar_asistencias()

    assert resultado == datos