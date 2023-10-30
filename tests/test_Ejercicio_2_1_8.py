import pytest
from src.Ejercicio_2_1_8 import nivelRendimiento, cantidadDinero

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (0.0, "inaceptable"),
        (0.4, "aceptable"),
        (0.6, "meritorio"),
        (0.9, "meritorio")
    ]
)

def test_nivelRendimiento_params(input_x, expected):
    assert nivelRendimiento(input_x) == expected

@pytest.mark.parametrize(
    "input_y, expected",
    [
        (0.0, 0.0),
        (0.4, 960),
        (0.6, 1440),
        (0.9, 2160)
    ]
)

def test_cantidadDinero_params(input_y, expected):
    assert cantidadDinero(input_y) == expected