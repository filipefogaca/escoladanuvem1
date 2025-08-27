def calcula_gorjeta (valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta/100)
    return gorjeta

total_conta = float(input("digite o valor total da conta: R$ "))
porcentagem = float(input("digite a porcentagem da gorjeta: "))

gorjeta_valor = calcula_gorjeta(total_conta, porcentagem)

print(f"Para conta: R${total_conta:.2f}, a gorjeta de {porcentagem:.2f}%, é R${gorjeta_valor:.2f}")
