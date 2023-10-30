import pytest
from src.Ejercicio_2_1_6 import comprobarInicial, comprobarSexo

@pytest.mark.parametrize(
    "input_x, expected",
    [
        ('Aitana', True),
        ('AITANA', True),
        ('aitor', True),
        ('sara', False),
        ('Tomás', False)
    ]
)

def comprobarInicial_params(input_x, expected):
    assert comprobarInicial(input_x) == expected


@pytest.mark.parametrize(
    "input_y, expected",
    [
        ('HOMBRE', False),
        ('mujer', True),
        ('hombre', False),
        ('Mujer', True),
        ('Hombre', False)
    ]
)
def test_comprobarSexo_params(input_y, expected):
    assert comprobarSexo(input_y) == expected