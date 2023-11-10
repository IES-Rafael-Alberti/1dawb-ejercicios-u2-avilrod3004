import pytest
from src.Ejercicio_2_2_23 import longitudTitulo, encontrarNumero

@pytest.mark.parametrize(
    'input_x, expected',
    [
        ('20000 leguas de viaje submarino', 31),
        ('El espia que surgio del frio', 28),
        ('Viaje al centro de la Tierra', 28),
        ('El lobo de mar', 14),
        ('Puerta al verano', 16)
    ]
)

def test_longitudTitulo_params(input_x, expected):
    assert longitudTitulo(input_x) == expected


@pytest.mark.parametrize(
    'input_y, input_z, expected',
    [
        ('20000 leguas de viaje submarino', 31, 5),
        ('El espia que surgio del frio', 28, 0),
        ('Los 3 mosqueteros', 17, 1),
        ('El lobo de mar', 14, 0),
        ('Puerta al verano', 16, 0)
    ]
)

def test_encontrarNumero_params(input_y, input_z, expected):
    assert encontrarNumero(input_y, input_z) == expected