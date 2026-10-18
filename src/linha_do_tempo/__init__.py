"""Interface pública dos cálculos de datas."""

from .idade import calcular_idade
from .prazos import dias_ate, dias_desde

__all__ = ["calcular_idade", "dias_ate", "dias_desde"]
