import pytest
from src.Ejercicio_2_2_17 import sumaDigitos

@pytest.mark.parametrize(
    'input_x, expected',
    [
        (1234, 10),
        (123, 6),
        (451, 10),
        (2023, 7),
        (1302, 6)
    ]
)

def test_sumaDigitos_params(input_x, expected):
    assert sumaDigitos(input_x) == expected