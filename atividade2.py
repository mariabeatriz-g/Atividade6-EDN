import requests

def gerar_usuario():
    url = 'https://randomuser.me/api/'
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Gera erro se a resposta for ruim (ex: 404)

        dados = resposta.json()
        usuario = dados['results'][0]

        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("=== Perfil de Usuário Gerado ===")
        print("Nome :", nome_completo)
        print("Email:", email)
        print("País :", pais)

    except requests.exceptions.RequestException as e:
        print("Erro ao acessar a API:", e)

# Executa o programa
gerar_usuario()