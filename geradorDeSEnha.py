import random
import string

def gerar_senha(length=50):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(length))
    return senha

senha_aleatoria = gerar_senha()
print(senha_aleatoria)