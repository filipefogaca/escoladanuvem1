soma_notas = 0

for i in range(1, 5):
    nota=float(input(f"digite a {i}° nota do  aluno: "))
    soma_notas += nota
media = soma_notas/4

print("-" * 30)
print(f"A soma das 4 notas foi: {soma_notas}")
print(f"A média do aluno é: {media:.1f}")



