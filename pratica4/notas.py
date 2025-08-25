def registrador_de_notas():
    notas = []
    while True:
        entrada = input("Digite uma nota de 0 a 10 (ou 'fim' para terminar): ")
        if entrada.lower() == 'fim':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. A nota deve ser entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nA média da turma é: {media:.2f}")
    else:
        print("\nNenhuma nota foi inserida.")

registrador_de_notas()
