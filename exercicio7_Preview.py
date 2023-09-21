# givanio josé de melo
# sexta-feira 18 de agosto de 2023
# codigo de exemplo para ser utilizado
# no exercicio 7 de prática de lógica
# de programação com o 2º ano B

alunos = []
notas = []

# Essa é a variavel de controle do laço de repetição
# se este valor for alterado, 
# o código a partir da linha 9 até a linha 23
# não será executado nenhuma vez
concluir = False


while (not concluir):
    # solicitando que digite o nome do aluno
    print("Digite o nome do aluno:")
    nomeAluno = input()

    #solicitando que digite a nota do aluno
    print("Digite a nota do aluno")
    notaAluno = int(input())

    # verificação da nota e frases equivalentes a cara perfil de nota
    if(notaAluno < 5): print("Misericórdia")
    elif(notaAluno < 7): print("Tá quase")
    else: print("Passsssssou")

    #inserindo os dados de nome e 
    # nota do aluno em suas respectivas listas
    alunos.append(nomeAluno)
    notas.append(notaAluno)

    print("Deseja inserir outra nota?(s/n)")
    concluir = input() == "n"

print("Seguem abaixo todas as notas digitadas:")
print("Aluno : Nota")
for i in range(len(alunos)):
    print(f"{alunos[i]} : {notas[i]}")

input("Pressione Enter pra terminar...")


