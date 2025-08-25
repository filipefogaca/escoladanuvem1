def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida.")

            print(f"O resultado é: {resultado}")
            break

        except ValueError as ve:
            if "could not convert string to float" in str(ve):
                print("Erro: Entrada inválida. Por favor, insira apenas números.")
            else:
                print(f"Erro: {ve}. As operações válidas são +, -, *, /.")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

calculadora()
