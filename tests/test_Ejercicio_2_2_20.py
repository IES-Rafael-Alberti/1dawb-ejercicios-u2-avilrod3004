import pytest
from src.Ejercicio_2_2_20 import numCaracteres

@pytest.mark.parametrize(
    'input_x, expected',
    [
        ('mobilis in mobile', 17),
        ('Hola mundo', 10),
        ('Era se una vez', 14),
        ('En un lugar de la mancha, cuyo nombre no quiero acordarme', 57),
        ('Marco Polo', 10)
    ]
)

def test_numCaracteres_params(input_x, expected):
    assert numCaracteres(input_x) == expected