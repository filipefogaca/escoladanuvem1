valor_temp_str = input("Digite o valor da temperatura: ")
unidade_origem = input("Digite a unidade de origem (C, F, K): ").upper()
unidade_destino = input("Digite a unidade de destino (C, F, K): ").upper()

valor_temp = float(valor_temp_str)
temp_em_celsius = 0


if unidade_origem == 'F':
    temp_em_celsius = (valor_temp - 32) * 5 / 9
elif unidade_origem == 'K':
    temp_em_celsius = valor_temp - 273.15
else: # Se a origem já for 'C', não faz nada
    temp_em_celsius = valor_temp


resultado = 0
if unidade_destino == 'F':
    resultado = (temp_em_celsius * 9 / 5) + 32
elif unidade_destino == 'K':
    resultado = temp_em_celsius + 273.15
else:
    resultado = temp_em_celsius

print(f"{valor_temp:.2f} {unidade_origem} é igual a {resultado:.2f} {unidade_destino}")