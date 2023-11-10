import pytest
from src.Ejercicio_2_2_24 import esPrimo

@pytest.mark.parametrize(
    'num, expected',
    [
        (11, True),
        (8, False),
        (47, True),
        (2, True),
        (21, False)
    ]
)

def test_esPrimo_params(num, expected):
    assert esPrimo(num) == expected