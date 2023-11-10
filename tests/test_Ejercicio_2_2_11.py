import pytest
from src.Ejercicio_2_2_11 import contarLetras

@pytest.mark.parametrize(
    'input_x, expected',
    [
        ('hola', 4),
        ('qwerty', 6),
        ('supercalifragilisticoespialidoso', 32),
        ('python', 6)
    ]
)

def test_contarLetras_params(input_x, expected):
    assert contarLetras(input_x) == expected