from datetime import date

import pytest

from calendario import calcular_idade


@pytest.mark.parametrize(
    ("nascimento", "referencia", "esperado"),
    [
        (date(2000, 6, 15), date(2026, 6, 15), 26),
        (date(2000, 6, 16), date(2026, 6, 15), 25),
        (date(2000, 1, 1), date(2026, 12, 31), 26),
    ],
)
def test_idade_em_anos_completos(nascimento, referencia, esperado):
    assert calcular_idade(nascimento, referencia) == esperado


def test_aniversario_bissexto_considera_primeiro_de_marco():
    nascimento = date(2000, 2, 29)
    assert calcular_idade(nascimento, date(2025, 2, 28)) == 24
    assert calcular_idade(nascimento, date(2025, 3, 1)) == 25


def test_nascimento_futuro_nao_e_aceito():
    with pytest.raises(ValueError):
        calcular_idade(date(2026, 6, 16), date(2026, 6, 15))
