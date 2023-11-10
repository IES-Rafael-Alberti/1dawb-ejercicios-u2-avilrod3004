import pytest
from src.Ejercicio_2_2_25 import separarPorEspacios, contarPalabras, contarLetras

@pytest.mark.parametrize(
    'input_a, expected',
    [
        ('mobilis in mobile', ['mobilis', 'in', 'mobile']),
        ('hello world', ['hello', 'world']),
        ('Era se una vez', ['Era', 'se', 'una', 'vez']),
        ('He visto cosas que no creeriais', ['He', 'visto', 'cosas', 'que', 'no', 'creeriais'])
    ]
)

def test_separarPorEspacios_params(input_a, expected):
    assert separarPorEspacios(input_a) == expected


@pytest.mark.parametrize(
    'input_b, expected',
    [
        (['mobilis', 'in', 'mobile'], 3),
        (['hello', 'world'], 2),
        (['Era', 'se', 'una', 'vez'], 4),
        (['He', 'visto', 'cosas', 'que', 'no', 'creeriais'], 6)
    ]
)

def test_contarPalabras_params(input_b, expected):
    assert contarPalabras(input_b) == expected



@pytest.mark.parametrize(
    'input_c, input_d, expected',
    [
        (['mobilis', 'in', 'mobile'], 3, 'mobilis'),
        (['hello', 'world'], 2, 'hello'),
        (['Era', 'se', 'una', 'vez'], 4, 'Era'),
        (['He', 'visto', 'cosas', 'que', 'no', 'creeriais'], 6, 'creeriais')
    ]
)

def test_contarLetras_params(input_c, input_d, expected):
    assert contarLetras(input_c, input_d) == expected