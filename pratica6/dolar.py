import requests

def consultar_cotacao():
    codigo_moeda = input("Digite o código da moeda desejada (ex: USD, EUR, GBP): ").upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"
    response = requests.get(url)
    if response.status_code == 200:
        # Converte a resposta JSON para um dicionário Python
        dados = response.json()
        chave_dicionario = f"{codigo_moeda}BRL"
        cotacao = dados[chave_dicionario]
        nome_moeda = cotacao['name']
        valor_atual = cotacao['bid']  # 'bid' é o preço de compra, o mais comum para cotação
        maximo = cotacao['high']
        minimo = cotacao['low']
        data_atualizacao = cotacao['create_date']

        print("\n--- Cotação Atual ---")
        print(f"Moeda: {nome_moeda}")
        print(f"Valor Atual (Compra): R$ {valor_atual}")
        print(f"Máximo do Dia: R$ {maximo}")
        print(f"Mínimo do Dia: R$ {minimo}")
        print(f"Última Atualização: {data_atualizacao}")
        print("---------------------\n")
    else:
        print(f"\nErro: Não foi possível obter a cotação para a moeda '{codigo_moeda}'.")
        print("Por favor, verifique se o código está correto e tente novamente.")

consultar_cotacao()