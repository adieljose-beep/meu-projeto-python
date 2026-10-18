# Linha do Tempo

Projeto Python para calcular idade em anos completos e contar dias entre datas.

## Instalação

Requer Python 3.10 ou superior. Para instalar as dependências dos testes:

```bash
python -m pip install -e ".[test]"
python -m pytest
```

## Exemplo

```python
from datetime import date
from calendario import calcular_idade, dias_ate

idade = calcular_idade(date(1990, 8, 20))
prazo = dias_ate(date(2030, 1, 1))
```

As funções aceitam uma data de referência opcional para uso determinístico. A idade é calculada em anos completos; em anos sem 29 de fevereiro, o aniversário de quem nasceu nessa data é considerado em 1º de março. Datas em direção incompatível com a contagem geram `ValueError`.

A função `dias_desde` foi introduzida na branch `NovoCalculo` e chegou a `master` pelo merge sem fast-forward exigido na atividade.
