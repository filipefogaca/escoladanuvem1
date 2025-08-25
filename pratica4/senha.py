def verificador_de_senha():
    while True:
        senha = input("Crie uma senha (ou digite 'sair' para cancelar): ")
        if senha.lower() == 'sair':
            print("Criação de senha cancelada.")
            break

        tem_numero = False
        for char in senha:
            if char.isdigit():
                tem_numero = True
                break

        if len(senha) >= 8 and tem_numero:
            print("Senha forte criada com sucesso!")
            break
        else:
            print("Senha fraca. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")

verificador_de_senha()
