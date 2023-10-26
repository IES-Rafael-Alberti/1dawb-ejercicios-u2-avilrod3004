import pytest
from src.Ejercicio_2_1_4 import calcularResto, restoCero

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (1, False),
        (18, True),
        (100, True),
        (5, False),
        (17, False),
        (125, True)
    ]
)
def test_calcularResto_params(input_n, expected):
    assert calcularResto(input_n) == expected



@pytest.mark.parametrize(
    "input_n, expected",
    [
        (1, False),
        (18, True),
        (100, True),
        (5, False),
        (17, False),
        (125, True)
    ]
)
def test_restoCero_params(input_n, expected):
    assert restoCero(input_n) == expected