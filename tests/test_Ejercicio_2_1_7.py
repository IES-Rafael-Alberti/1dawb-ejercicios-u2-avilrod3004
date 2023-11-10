import pytest
from src.Ejercicio_2_1_7 import tipoRenta

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (900, 5),
        (15000, 15),
        (20001, 20),
        (65001, 45)
    ]
)

def test_nombre_tipoRenta_params(input_x, expected):
    assert tipoRenta(input_x) == expected