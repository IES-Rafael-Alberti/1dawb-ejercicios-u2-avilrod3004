import pytest
from src.Ejercicio_2_2_1 import repetirPalabra

@pytest.mark.parametrize(
    'palabra, expected',
    [
        ('uwu', 'uwu\nuwu\nuwu\nuwu\nuwu\nuwu\nuwu\nuwu\nuwu\nuwu\n'),
        ('qwerty', 'qwerty\nqwerty\nqwerty\nqwerty\nqwerty\nqwerty\nqwerty\nqwerty\nqwerty\nqwerty\n'),
        ('hola', 'hola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\n')
    ]
)

def test_repetirPalabra_params(palabra, expected):
    assert repetirPalabra(palabra) == expected