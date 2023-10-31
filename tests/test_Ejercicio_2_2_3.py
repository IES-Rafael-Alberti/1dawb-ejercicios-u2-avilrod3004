import pytest
from src.Ejercicio_2_2_3 import numImpares

@pytest.mark.parametrize(
    'num, expected',
    [
        (4, '4 -->  1, 3, 4'),
        (10, '10 -->  1, 3, 5, 7, 9, 10'),
        (15, '15 -->  1, 3, 5, 7, 9, 11, 13, 15'),
        (25, '25 -->  1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25')
    ]
)

def test_numImapres_params(num, expected):
    assert numImpares(num) == expected