def calcular_idade(data_nascimento):
    idade = (2025 - data_nascimento) * 365
    return idade

ano_nascimento = int(input("digite a data do ano de nascimento ex:(2003): "))

idade_dias = calcular_idade(ano_nascimento)

print(f"Idade em dias é: {idade_dias} dias")
