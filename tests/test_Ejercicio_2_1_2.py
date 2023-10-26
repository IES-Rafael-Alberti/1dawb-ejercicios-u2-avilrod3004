import pytest
from src.Ejercicio_2_1_2 import coincidePasswd

@pytest.mark.parametrize(
    "input_n, expected",
    [
        ('contraseña', True),
        ('CONTRASEÑA', True),
        ('ConTRAseÑa', True),
        ('HOLA', False),
        ('abcdefghi', False),
        ('admin', False)
    ]
)
def test_coincidePasswd_params(input_n, expected):
    assert coincidePasswd(input_n) == expected