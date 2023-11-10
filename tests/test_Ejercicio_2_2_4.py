import pytest 
from src.Ejercicio_2_2_4 import cuentaAtras

@pytest.mark.parametrize(
    'num, expected',
    [
        (5, 'Cuenta atrás --> 5, 4, 3, 2, 1, 0'),
        (10, 'Cuenta atrás --> 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0'),
        (7, 'Cuenta atrás --> 7, 6, 5, 4, 3, 2, 1, 0'),
        (21, 'Cuenta atrás --> 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0')
    ]
)

def test_cuentaAtras_params(num, expected):
    assert cuentaAtras(num) == expected