def contador_par_impar():
    pares = 0
    impares = 0
    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para sair): ")
        if entrada.lower() == 'fim':
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é par.")
                pares += 1
            else:
                print(f"{numero} é ímpar.")
                impares += 1
        except ValueError:
            print("Erro: Por favor, insira um número inteiro válido.")

    print(f"\nTotal de números pares inseridos: {pares}")
    print(f"Total de números ímpares inseridos: {impares}")

contador_par_impar()
