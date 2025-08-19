numeroFunc = int(input("digite o número do funcionário: "))
horasT = int(input("digite as horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor que recebe por hora: "))

salario = horasT * valor_por_hora
print(f"Número = {numeroFunc}")
print(f"SALÁRIO = R$ {salario:.2f}")