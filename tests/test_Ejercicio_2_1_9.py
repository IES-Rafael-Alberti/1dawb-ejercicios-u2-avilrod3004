import pytest
from src.Ejercicio_2_1_9 import calcularPrecio

@pytest.mark.parametrize(
    'input_x, expected',
    [
        (2, 'gratis'),
        (3, 'gratis'),
        (4, '5€'),
        (17, '5€'),
        (80, '10€')
    ]
)

def test_calcularPrecio_params(input_x, expected):
    assert calcularPrecio(input_x) == expected