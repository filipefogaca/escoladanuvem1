nome = input("Digite o nome do vendedor: ")
salario_fixo_str = input("Digite o salário fixo: ")
total_vendas_str = input("Digite o total de vendas no mês (em dinheiro): ")

salario_fixo = float(salario_fixo_str)
total_vendas = float(total_vendas_str)

comissao = total_vendas * 0.15
total_receber = salario_fixo + comissao

print(f"TOTAL = R$ {total_receber:.2f}")