import pytest
from src.Ejercicio_2_2_19 import ejecutarOpciones

@pytest.mark.parametrize(
    'input_x, expected',
    [
        ('1', True),
        ('2', True),
        ('3', False)
    ]
)

def test_ejecutarOpciones_params(input_x, expected):
    assert ejecutarOpciones(input_x) == expected