import requests

def gerar_perfil():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    dados = response.json()
    usuario = dados['results'][0]

    print("--- Perfil de Usuário Gerado ---")
    print(f"Nome: {usuario['name']['first']} {usuario['name']['last']}")
    print(f"Email: {usuario['email']}")
    print(f"País: {usuario['location']['country']}")
    print("---------------------------------")

gerar_perfil()