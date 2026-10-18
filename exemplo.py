from datetime import date


def calcular_idade(data_nascimento):
    hoje = date.today()
    return hoje.year - data_nascimento.year - (
        (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)
    )


def dias_ate(data_futura):
    hoje = date.today()
    return (data_futura - hoje).days


if __name__ == "__main__":
    idade = calcular_idade(date(1990, 8, 20))
    prazo = dias_ate(date(2030, 1, 1))

    print(f"Idade: {idade} anos")
    print(f"Dias até 01/01/2030: {prazo} dias")
