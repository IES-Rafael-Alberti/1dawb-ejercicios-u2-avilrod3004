import pytest
from src.Ejercicio_2_2_5 import calcularInversion

@pytest.mark.parametrize(
    'input_x, input_y, input_z, expected',
    [
        (1000, 5, 1, 1000.05),
        (1000, 5, 4, 4000.05),
        (1845, 8, 3, 5535.08),
        (1845, 8, 7, 12915.08),
        (29000, 5, 2, 58000.05)
    ]
)

def test_calcularInversion_params(input_x, input_y, input_z, expected):
    assert calcularInversion(input_x, input_y, input_z) == expected