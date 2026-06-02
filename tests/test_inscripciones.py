import sys
import os

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "src"
    )
)

from unittest.mock import Mock, patch

from servicios.servicio_inscripciones import (
    inscribir_miembro,
    listar_inscripciones
)


@patch("servicios.servicio_inscripciones.buscar_miembro_por_id")
def test_inscribir_miembro_inexistente(
    mock_buscar_miembro
):
    mock_buscar_miembro.return_value = None

    resultado = inscribir_miembro(1, 101)

    assert resultado == "El miembro no existe."


@patch("servicios.servicio_inscripciones.buscar_clase_por_id")
@patch("servicios.servicio_inscripciones.buscar_miembro_por_id")
def test_inscribir_clase_inexistente(
    mock_buscar_miembro,
    mock_buscar_clase
):
    mock_buscar_miembro.return_value = {"id": 1}
    mock_buscar_clase.return_value = None

    resultado = inscribir_miembro(1, 101)

    assert resultado == "La clase no existe."


@patch("servicios.servicio_inscripciones.cargar_inscripciones")
@patch("servicios.servicio_inscripciones.buscar_clase_por_id")
@patch("servicios.servicio_inscripciones.buscar_miembro_por_id")
def test_inscribir_sin_cupo(
    mock_buscar_miembro,
    mock_buscar_clase,
    mock_cargar_inscripciones
):
    mock_buscar_miembro.return_value = {"id": 1}

    clase_mock = Mock()
    clase_mock.capacidad_maxima = 2

    mock_buscar_clase.return_value = clase_mock

    mock_cargar_inscripciones.return_value = [
        {"id_miembro": 1, "id_clase": 101},
        {"id_miembro": 2, "id_clase": 101}
    ]

    resultado = inscribir_miembro(3, 101)

    assert resultado == "No hay cupo disponible en esta clase."


@patch("servicios.servicio_inscripciones.guardar_inscripciones")
@patch("servicios.servicio_inscripciones.cargar_inscripciones")
@patch("servicios.servicio_inscripciones.buscar_clase_por_id")
@patch("servicios.servicio_inscripciones.buscar_miembro_por_id")
def test_inscripcion_exitosa(
    mock_buscar_miembro,
    mock_buscar_clase,
    mock_cargar_inscripciones,
    mock_guardar_inscripciones
):
    mock_buscar_miembro.return_value = {"id": 1}

    clase_mock = Mock()
    clase_mock.capacidad_maxima = 10

    mock_buscar_clase.return_value = clase_mock

    mock_cargar_inscripciones.return_value = []

    resultado = inscribir_miembro(1, 101)

    assert resultado == "Inscripción realizada con éxito."

    mock_guardar_inscripciones.assert_called_once()

    inscripciones_guardadas = (
        mock_guardar_inscripciones.call_args[0][0]
    )

    assert len(inscripciones_guardadas) == 1

    assert inscripciones_guardadas[0] == {
        "id_miembro": 1,
        "id_clase": 101
    }


@patch("servicios.servicio_inscripciones.cargar_inscripciones")
def test_listar_inscripciones(
    mock_cargar_inscripciones
):
    datos = [
        {
            "id_miembro": 1,
            "id_clase": 101
        }
    ]

    mock_cargar_inscripciones.return_value = datos

    assert listar_inscripciones() == datos

import sys
import os

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "src"
    )
)

from datos import repositorio_inscripciones


def test_cargar_inscripciones_archivo_inexistente(
    monkeypatch,
    tmp_path
):
    ruta = tmp_path / "inscripciones.json"

    monkeypatch.setattr(
        repositorio_inscripciones,
        "RUTA",
        str(ruta)
    )

    resultado = repositorio_inscripciones.cargar_inscripciones()

    assert resultado == []


def test_cargar_inscripciones_archivo_vacio(
    monkeypatch,
    tmp_path
):
    ruta = tmp_path / "inscripciones.json"

    ruta.write_text("")

    monkeypatch.setattr(
        repositorio_inscripciones,
        "RUTA",
        str(ruta)
    )

    resultado = repositorio_inscripciones.cargar_inscripciones()

    assert resultado == []


def test_guardar_y_cargar_inscripciones(
    monkeypatch,
    tmp_path
):
    ruta = tmp_path / "inscripciones.json"

    monkeypatch.setattr(
        repositorio_inscripciones,
        "RUTA",
        str(ruta)
    )

    datos = [
        {
            "id_miembro": 1,
            "id_clase": 101
        }
    ]

    repositorio_inscripciones.guardar_inscripciones(datos)

    resultado = repositorio_inscripciones.cargar_inscripciones()

    assert resultado == datos