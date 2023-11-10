import pytest
from src.Ejercicio_2_2_22 import numDigitos

@pytest.mark.parametrize(
    'input_x, expected',
    [
        (123, 3),
        (88, 2),
        (159789, 6),
        (1, 1),
        (578, 3)
    ]
)

def test_numDigitos_params(input_x, expected):
    assert numDigitos(input_x) == expected