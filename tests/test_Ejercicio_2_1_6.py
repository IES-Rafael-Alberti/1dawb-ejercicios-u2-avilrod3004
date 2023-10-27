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

def comprobarInicial_params(input_n, expected):
    assert comprobarInicial(input_n) == expected


@pytest.mark.parametrize(
    "input_n, expected",
    [
        ('HOMBRE', False),
        ('mujer', True),
        ('hombre', False),
        ('Mujer', True),
        ('Hombre', False)
    ]
)
def test_comprobarSexo_params(input_n, expected):
    assert comprobarSexo(input_n) == expected