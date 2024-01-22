#declarando uma funcao
def perguntar():
    return input("O que deseja realizar?\n" 
            +
            "<I> - Para Inserir um usuário\n"
            +
            "<P> - Para Pesquisar um usuário\n"
            +
            "<E> - Para Excluir um usuário\n"
            +
            "<L> - Para Listar um usuário\n"
            + 
            "<Qualquer outro caracter para sair>").upper()
    
#declarando uma função de inserção de dados em um dicionario
def inserir(dicionario): 
 #para simplificar o código eu posso chamar todos os inputs diretamente no dicionario. Abaixo comentado, o codigo não simplificado (declarando variaveis e depoiis inserindo-as no codigo)
       # chave=input("Digite o login: ").upper()
       # nome=input("Digite o nome: ").upper()
       # data=input("Digite a última data de acesso: ")
       # estacao=input("Qual a última estação acessada: ").upper()
       # usuarios[chave]=[nome, data, estacao]
        

    #Agora o codigo simplificado (com as variaveis declaradas dentro do dicionario)
    dicionario[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(), 
                                                     input("Digite a última data de acesso: "), 
                                                     input("Qual a última estação acessada: ").upper()]
    salvar(dicionario)
        
def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)

def salvar (dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))