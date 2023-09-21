# usando a estrutura condicional IF,
# nós podemos controlar o fluxo de execução de código...

a = input("digite a sua coisa favorita: ")

if (a == "café"):
    print("Parabens! Você é professor...")
else:
    print("Está errado, tente outra hora...")

#implemente um sistema que faça 10 perguntas e diga se o usuário acertou ou não as respostas...

#uma variável pode ser incrementada de valor, exemplo
x = 1 #o valor de x é igual a 1
x = x + 1 # o novo valor de x passou a ser a 2
x = x + x # o valor de x passou de 2 para 4
x = x + 2 # o valor de x passou de 4 para 6

#use uma variável incremental para dar uma nota no final do questionário...

pergunta1  = "Qual o melhor anime de todos os tempos?"
pergunta2  = "Quem é o guerreiro mais poderoso do universo 7?"
pergunta3  = "Luffy quer ser o rei dos...?"
pergunta4  = "Qual sequencia de anime é uma decepção total?"
pergunta5  = "Colocar abacaxi na pizza é...?"
pergunta6  = "Quem cozinha macarrão na agua fria merece a...?"
pergunta7  = "A Policia trabalha certa, se aborda é por que tem...?"
pergunta8  = "Qual o melhor amigo do homem?"
pergunta9  = "Quem espera, sempre...?"
pergunta10 = "Kenshin Himura era conhecido como..."

resposta_certa_1 = "Naruto"
resposta_certa_2 = "Goku"
resposta_certa_3 = "piratas"
resposta_certa_4 = "Boruto"
resposta_certa_5 = "pecado"
resposta_certa_6 = "morte"
resposta_certa_7 = "certeza"
resposta_certa_8 = "playstation"
resposta_certa_9 = "cansa"
resposta_certa_10 = "Battousai"

resposta_usuario_1 = input(pergunta1)
resposta_usuario_2 = input(pergunta2)
resposta_usuario_3 = input(pergunta3)
resposta_usuario_4 = input(pergunta4)
resposta_usuario_5 = input(pergunta5)
resposta_usuario_6 = input(pergunta6)
resposta_usuario_7 = input(pergunta7)
resposta_usuario_8 = input(pergunta8)
resposta_usuario_9 = input(pergunta9)
resposta_usuario_10 = input(pergunta10)

nota = 0
if (resposta_usuario_1 == resposta_certa_1): print("Acertou Miseravi !!!"); nota = nota + 1
if (resposta_usuario_2 == resposta_certa_2): print("Acertou Miseravi !!!"); nota = nota + 1
if (resposta_usuario_3 == resposta_certa_3): print("Acertou Miseravi !!!"); nota = nota + 1
if (resposta_usuario_4 == resposta_certa_4): print("Acertou Miseravi !!!"); nota = nota + 1
if (resposta_usuario_5 == resposta_certa_5): print("Acertou Miseravi !!!"); nota = nota + 1
if (resposta_usuario_6 == resposta_certa_6): print("Acertou Miseravi !!!"); nota = nota + 1
if (resposta_usuario_7 == resposta_certa_7): print("Acertou Miseravi !!!"); nota = nota + 1
if (resposta_usuario_8 == resposta_certa_8): print("Acertou Miseravi !!!"); nota = nota + 1
if (resposta_usuario_9 == resposta_certa_9): print("Acertou Miseravi !!!"); nota = nota + 1
if (resposta_usuario_10 == resposta_certa_10): print("Acertou Miseravi !!!"); nota = nota + 1

if(nota == 0):
    print("parabens, nota dó...")
else:
    print(f"sua nota foi: {nota}")

input("Pressione Enter para continuar....")