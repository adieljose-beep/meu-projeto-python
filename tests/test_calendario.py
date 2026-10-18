from datetime import date

import pytest

from calendario import dias_ate, dias_desde


def test_dias_ate_atravessa_a_virada_do_ano():
    assert dias_ate(date(2027, 1, 1), date(2026, 12, 31)) == 1


def test_dias_ate_hoje_retorna_zero():
    referencia = date(2026, 6, 15)
    assert dias_ate(referencia, referencia) == 0


def test_dias_ate_rejeita_data_passada():
    with pytest.raises(ValueError):
        dias_ate(date(2026, 6, 14), date(2026, 6, 15))


def test_dias_desde_data_passada():
    assert dias_desde(date(2026, 6, 10), date(2026, 6, 15)) == 5


def test_dias_desde_hoje_retorna_zero():
    referencia = date(2026, 6, 15)
    assert dias_desde(referencia, referencia) == 0


def test_dias_desde_rejeita_data_futura():
    with pytest.raises(ValueError):
        dias_desde(date(2026, 6, 16), date(2026, 6, 15))
