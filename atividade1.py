import random
import string

def gerar_senha(tamanho):
    # Conjunto de caracteres: letras minúsculas, maiúsculas, dígitos e especiais
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Geração aleatória da senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Solicita ao usuário o tamanho da senha
try:
    tamanho = int(input("Digite o número de caracteres da senha: "))
    if tamanho <= 0:
        print("Por favor, digite um número positivo maior que zero.")
    else:
        senha_gerada = gerar_senha(tamanho)
        print("Senha gerada:", senha_gerada)
except ValueError:
    print("Entrada inválida. Digite um número inteiro.")