import pytest
from src.Ejercicio_2_1_3 import divisorCero

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (0, True),
        (18, False),
        (100, False),
        (5, False)
    ]
)
def test_divisorCero_params(input_n, expected):
    assert divisorCero(input_n) == expected