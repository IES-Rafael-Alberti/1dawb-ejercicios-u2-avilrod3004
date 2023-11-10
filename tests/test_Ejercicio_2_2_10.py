import pytest
from src.Ejercicio_2_2_10 import esPrimo

@pytest.mark.parametrize(
    'num, expected',
    [
        (11, 'Es primo'),
        (8, 'No es primo'),
        (47, 'Es primo'),
        (2, 'Es primo'),
        (21, 'No es primo')
    ]
)

def test_esPrimo_params(num, expected):
    assert esPrimo(num) == expected