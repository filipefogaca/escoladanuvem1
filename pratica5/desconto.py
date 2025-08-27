def calcular_desconto(valor_produto, percentual_desconto):
    valor_final = valor_produto - valor_produto * (percentual_desconto/100)
    return valor_final

produto = float(input("digite o valor do produto: R$"))
porcentagem = float(input("digite a porcentagem de desconto: "))

valor_desconto = calcular_desconto(produto, porcentagem)

print(f"para o valor R${produto:.2f}, o valor com desconto de {porcentagem}% é: R${valor_desconto:.2f}  ")





