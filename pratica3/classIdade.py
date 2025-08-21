idade_str = input("Digite a sua idade: ")
idade = int(idade_str)

if 0 <= idade <= 12:
    classificacao = "Criança"
elif 13 <= idade <= 17:
    classificacao = "Adolescente"
elif 18 <= idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

print(f"A classificação para a idade {idade} é: {classificacao}")