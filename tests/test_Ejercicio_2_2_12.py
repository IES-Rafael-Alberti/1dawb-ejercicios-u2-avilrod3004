import pytest
from src.Ejercicio_2_2_12 import contarLetra

@pytest.mark.parametrize(
    'input_x, input_y, expected',
    [
        ('mobilis in mobile', 'i', 4),
        ('Si os dan papel pautado escribid por el otro lado', 'o', 6),
        ('hello world', 'l', 3),
        ('Todo me male sal', 'm', 2)
    ]
)

def test_contarLetra_params(input_x, input_y, expected):
    assert contarLetra(input_x, input_y) == expected