"""Contagens de dias em relação a uma data de referência."""

from datetime import date


def _referencia(hoje: date | None) -> date:
    return date.today() if hoje is None else hoje


def dias_ate(data_futura: date, hoje: date | None = None) -> int:
    """Conta os dias entre hoje e uma data futura ou igual a hoje."""
    quantidade = (data_futura - _referencia(hoje)).days
    if quantidade < 0:
        raise ValueError("A data informada precisa ser hoje ou posterior.")
    return quantidade


def dias_desde(data_passada: date, hoje: date | None = None) -> int:
    """Conta os dias desde uma data passada ou igual à data de referência."""
    quantidade = (_referencia(hoje) - data_passada).days
    if quantidade < 0:
        raise ValueError("A data informada precisa ser hoje ou anterior.")
    return quantidade
