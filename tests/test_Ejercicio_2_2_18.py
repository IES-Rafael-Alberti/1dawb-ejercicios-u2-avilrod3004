import pytest
from src.Ejercicio_2_2_18 import sumaDigitos, numPar

@pytest.mark.parametrize(
    'input_x, expected',
    [
        (1234, 'La suma de los digitos de 1234 es 10'),
        (123, 'La suma de los digitos de 123 es 6'),
        (451, 'La suma de los digitos de 451 es 10'),
        (2023, 'La suma de los digitos de 2023 es 7'),
        (1302, 'La suma de los digitos de 1302 es 6')
    ]
)

def test_sumaDigitos_params(input_x, expected):
    assert sumaDigitos(input_x) == expected


@pytest.mark.parametrize(
    'input_y, input_z, expected',
    [
        (12, 2, 3),
        (5, 1, 1),
        (190, 5, 6),
        (137, 5, 5),
        (1326, 8, 9)
    ]
)

def test_numPar_params(input_y, input_z, expected):
    assert numPar(input_y, input_z) == expected