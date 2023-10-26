import pytest
from src.Ejercicio_2_1_1 import mayorEdad

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (2, False),
        (18, True),
        (100, True),
        (3, False),
        (17, False),
        (89, True)
    ]
)
def test_mayorEdad_params(input_n, expected):
    assert mayorEdad(input_n) == expected