peso_str = input("Digite seu peso em kg (ex: 70.5): ")
altura_str = input("Digite sua altura em metros (ex: 1.75): ")

peso = float(peso_str)
altura = float(altura_str)

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")