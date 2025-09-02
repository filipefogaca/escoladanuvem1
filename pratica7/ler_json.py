import json


def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
        return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{nome_arquivo}' não contém um JSON válido.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None


if __name__ == "__main__":
    nome_do_arquivo = input("Digite o nome do arquivo JSON a ser lido: ").strip()

    dados_lidos = ler_json(nome_do_arquivo)

    if dados_lidos:
        print("\nDados lidos do arquivo com sucesso:")
        print(f"  - Nome: {dados_lidos['nome']}")
        print(f"  - Idade: {dados_lidos['idade']}")
        print(f"  - Cidade: {dados_lidos['cidade']}")