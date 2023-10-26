import pytest
from src.Ejercicio_2_1_5 import comprobarEdad, comprobarIngresos

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (16, True),
        (17, True),
        (1, False),
        (5, False)
    ]
)

def test_comprobarEdad_params(input_x, expected):
    assert comprobarEdad(input_x) == expected