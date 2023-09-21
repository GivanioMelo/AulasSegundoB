perguntas = [
"Qual o melhor anime de todos os tempos?",
"Quem é o guerreiro mais poderoso do universo 7?",
"Luffy quer ser o rei dos...?",
"Qual sequencia de anime é uma decepção total?",
"Colocar abacaxi na pizza é...?",
"Quem cozinha macarrão na agua fria merece a...?",
"A Policia trabalha certa, se aborda é por que tem...?",
"Qual o melhor amigo do homem?",
"Quem espera, sempre...?",
"Kenshin Himura era conhecido como..."]

respostas_certas = ["Naruto","Goku",
"piratas","Boruto","pecado","morte",
"certeza","playstation","cansa","Battousai"]

nota = 0

for i in range(len(perguntas)):
    reposta = input(pergunta[i])
    if(resposta == respostas_certas[i]):
        print("Acertou mizeravi!!!")
        nota = nota + 1
    else:
        print("Errrrrrrrooou!!!")

if(nota == 0):
    print("parabens, nota dó...")
else:
    print(f"sua nota foi: {nota}")

input("Pressione Enter para continuar....")