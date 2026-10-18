"""Rotinas para calcular idades em anos completos."""

from datetime import date


def _aniversario_no_ano(data_nascimento: date, ano: int) -> date:
    """Monta o aniversário no ano de referência; 29/02 passa a 01/03."""
    try:
        return data_nascimento.replace(year=ano)
    except ValueError:
        return date(ano, 3, 1)


def calcular_idade(data_nascimento: date, hoje: date | None = None) -> int:
    """Calcula quantos anos completos a pessoa tem na data de referência."""
    referencia = date.today() if hoje is None else hoje
    if data_nascimento > referencia:
        raise ValueError("A data de nascimento não pode ser posterior à referência.")

    anos = referencia.year - data_nascimento.year
    aniversario = _aniversario_no_ano(data_nascimento, referencia.year)
    return anos - (referencia < aniversario)
