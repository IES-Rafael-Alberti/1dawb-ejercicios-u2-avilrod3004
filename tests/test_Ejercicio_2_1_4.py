import pytest
from src.Ejercicio_2_1_4 import calcularResto, restoCero

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (1, 1),
        (18, 0),
        (100, 0),
        (5, 1),
        (17, 1),
        (125, 1)
    ]
)
def test_calcularResto_params(input_x, expected):
    assert calcularResto(input_x) == expected



@pytest.mark.parametrize(
    "input_y, expected",
    [
        (1, False),
        (0, True)
    ]
)
def test_restoCero_params(input_y, expected):
    assert restoCero(input_y) == expected