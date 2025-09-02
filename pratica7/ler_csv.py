import csv

def ler_csv(nome_arquivo):
    dados = []
    try:
        with open(nome_arquivo, 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)

            next(leitor)
            for linha in leitor:
                dados.append(linha)
        return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None  # Retorna None em caso de erro
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None

if __name__ == "__main__":
    nome_do_arquivo = input("Digite o nome do arquivo: ").strip()

    dados_do_arquivo = ler_csv(nome_do_arquivo)
    for registro in dados_do_arquivo:
        print(registro)






