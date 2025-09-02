import json

def escrever_json(nome_arquivo, dados):
    if not nome_arquivo.endswith('.json'):
        nome_arquivo += '.json'

    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso em '{nome_arquivo}'")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

if __name__ == "__main__":
    dados_p = {
        "nome": "Filipe",
        "Idade": "20",
        "Cidade": "São Paulo"
    }
    nome_do_arquivo = input("Digite o nome do arquivo Json a ser salvo: ").strip()

    if nome_do_arquivo:
        escrever_json(nome_do_arquivo, dados_p)
    else:
        print("O nome do arquivo não pode ser vazio.")
