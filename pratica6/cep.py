'''
Desenvolva um programa que consulte informações
 de endereço a partir de um CEP fornecido pelo usuário,
  utilizando a API ViaCEP. O programa deve exibir o logradouro,
   bairro, cidade e estado correspondentes ao CEP consultado.
'''

import requests
import re

def consultar_cep():
    cep = input("Digite o CEP (apenas os 8 números): ")
    cep_limpo = re.sub(r'[^0-9]', '', cep)
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    response = requests.get(url)
    dados = response.json()
    if 'erro' in dados:
        print(f"O CEP {cep_limpo} não foi encontrado.")
    else:
        print("\n--- Endereço Encontrado ---")
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
consultar_cep()