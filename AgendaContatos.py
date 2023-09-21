import keyboard
import time
import os

def EsperaTecla(teclasValidas):
    while True:
        key_pressed = keyboard.read_key()
        if(key_pressed != ""):
            if(len(teclasValidas) == 0):
                return key_pressed
            if(key_pressed in teclasValidas):
                return key_pressed
        time.sleep(0.3)
def SelecionarTipoContato():
    time.sleep(1)
    print("Selecione o tipo do contato")
    print("0 -> Pessoal")
    print("1 -> Profissional")
    print("2 -> Romantico")
    Tipo = EsperaTecla(["0","1","2"])
    time.sleep(1)
    return Tipo
def LimparTela():
    os.system("cls")

tipos = ["Pessoal", "Profissional", "Romantico"]

# Criação e inserção de um novo contato
# podia ser tudo uma função só? podia...
# mas porque fazer tudo numa função só se você
# pode fazer cada pedacinho de cada vez?
# assim dá menos trabalho pra encontrar
# erros depois...
def criarContato(Nome, Telefone, Endereco, Tipo):
    contato = {}
    contato["Nome"] = Nome
    contato["Telefone"] = Telefone
    contato["Endereco"] = Endereco
    contato["Tipo"] = Tipo
    return contato
def preencherFormulario(contatos):
    LimparTela()
    time.sleep(1)
    print("Vamos Inserir um novo contato!")
    Nome = input("Digite o nome do contato: ")
    Telefone = input("Digite o telefone do contato: ")
    Endereco = input("Digite o endereço do contato: ")
    Tipo = SelecionarTipoContato()
    novoContato = criarContato(Nome, Telefone, Endereco, Tipo)
    return novoContato
def inserirContato(contatos):
    novocontato = preencherFormulario(contatos)
    contatos.append(novocontato)
    LimparTela()
    print(f"Contato Inserido: {novocontato}")
    print("Voltar (Esc)")
    opcao = EsperaTecla("esc")
    return contatos

# Remover Contato
def removerContatoPorNome(contatos, nome):
    contatos_mantidos = []
    for contato in contatos:
        if(contato["Nome"] != nome):
            contatos_mantidos.append(contato)
        else:
            print(f"Contato Excluido: {contato}")
    
    if(len(contatos_mantidos) == len(contatos)):
        print("Contato não encontrado!")
    
    print("Voltar (Esc)")
    opcao = EsperaTecla("esc")
    return contatos_mantidos
def iniciarRemocao(contatos):
    LimparTela()
    Nome = input("Digite o nome do contato que deseja remover:\n")
    return removerContatoPorNome(contatos,Nome)

# Editar Contato
def buscarContatoPorNome(contatos, nome):
    for contato in contatos:
        if(contato["Nome"] == nome):
            return contato
def alterarContatoPorNome(contatos, Nome, NomeNovo, Telefone, Endereco, Tipo):
    for contato in contatos:
        if(contato["Nome"] == Nome):
            contato["Nome"] = NomeNovo
            contato["Telefone"] = Telefone
            contato["Endereco"] = Endereco
            contato["Tipo"] = Tipo
    return contatos
def formularioEdicao(contatos, contato):
    NomeAntigo = contato["Nome"]
    Nome = contato["Nome"]
    Telefone = contato["Telefone"]
    Endereco = contato["Endereco"]
    Tipo = contato["Tipo"]

    Editando = True
    while Editando:
        LimparTela()
        time.sleep(1)
        print("Editando Contato")
        print(f"(Alterar - N) - Nome:\t\t {Nome}")
        print(f"(Alterar - F) - Telefone:\t {Telefone}")
        print(f"(Alterar - E) - Endereço:\t {Endereco}")
        print(f"(Alterar - T) - Tipo:\t\t {Tipo}")
        print("Encerrar edição (Esc)")
        opcao = EsperaTecla(["n","f","e","t","esc"])
        
        # Se apertou Esc é porque não quer mais editar, 
        # então sai da edição
        if(opcao == "esc"):
            Editando = False
        
        if(opcao in ["n","f","e"]):
            valorNovo = input("Digite o novo valor: ")
            if(opcao == "n"): Nome = valorNovo
            if(opcao == "f"): Telefone = valorNovo
            if(opcao == "e"): Endereco = valorNovo
        if(opcao == "t"):
            Tipo = SelecionarTipoContato()
    return alterarContatoPorNome(contatos, NomeAntigo, Nome,Telefone, Endereco, Tipo)
def iniciarEdicao(contatos):
    LimparTela()
    Nome = input("Digite o nome do contato que deseja editar:\n")
    contato = buscarContatoPorNome(contatos,Nome)
    return formularioEdicao(contatos, contato)

# Listar Contatos
def listarContatos(contatos):
    LimparTela()
    time.sleep(1)
    print("----------------------------------------")
    print("----------------CONTATOS----------------")
    print("----------------------------------------")
    for contato in contatos:
        print("----------------------------------------")
        print(contato["Nome"])
        print(contato["Telefone"])
        print(contato["Endereco"])
        print(tipos[int(contato["Tipo"])])
        print("----------------------------------------")
    print("Votlar (Esc)")
    opcao = EsperaTecla("esc")
    return

# MANIPULAÇÃO DE ARQUIVOS
def carregarContatos():
    contatos = []
    filename = "contatos.txt"
    if os.path.isfile(filename):
        file = open(filename, 'r')
        texto = file.read()
        file.close()

        linhas = texto.split("\n")
        for linha in linhas:
            if linha != "":
                dados = linha.split(";")
                contato = {}
                contato["Nome"] = dados[0]
                contato["Telefone"] = dados[1]
                contato["Endereco"] = dados[2]
                contato["Tipo"] = dados[3]
                contatos.append(contato)
    return contatos
def contatoParaRegistro(contato):
    nome = contato["Nome"].replace(";","")
    telefone = contato["Telefone"].replace(";","")
    endereco = contato["Endereco"].replace(";","")
    tipo = contato["Tipo"].replace(";","")
    registro = f"{nome};{telefone};{endereco};{tipo}\n"
    return registro
def salvarContatos(contatos):
    filename = "contatos.txt"
    file = open(filename, 'w')
    for contato in contatos:
        file.write(contatoParaRegistro(contato))
    file.close()

# Tela principal
def telaPrincipal(contatos):
    ProgramaRodando = True
    while ProgramaRodando:
        LimparTela()
        time.sleep(1)
        print("----------------------------------------")
        print("-----Bem vindo à agenda de contatos-----")
        print("----------------------------------------")
        print("Escolha uma das opções abaixo:")
        print("----------------------------------------")
        print("1 - Listar Contatos")
        print("2 - Inserir um Contato")
        print("3 - Editar um Contato")
        print("4 - Remover um Contato")
        print("5 - Salvar contatos em arquivo")
        print("Esc - Sair")
        print("----------------------------------------")
        opcao = EsperaTecla(["1","2","3","4","5","esc"])
        
        if(opcao == "1"): listarContatos(contatos)
        if(opcao == "2"): contatos = inserirContato(contatos)
        if(opcao == "3"): contatos = iniciarEdicao(contatos)
        if(opcao == "4"): contatos = iniciarRemocao(contatos)
        if(opcao == "5"): salvarContatos(contatos)
        if(opcao == "esc"):
            print("Deseja salvar antes de sair (S/N)?")
            confirmacao = EsperaTecla(["s","n","S","N"])
            if(confirmacao == "s" or confirmacao == "S"):
                salvarContatos(contatos)
            ProgramaRodando = False

LimparTela()
print("Aguarde, inicializando...")
contatos = carregarContatos()
time.sleep(3)
telaPrincipal(contatos)