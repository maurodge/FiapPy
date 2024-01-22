#importando as funcoes do arquivo de funcoes
from Funcoes import *

#criando um dicionario
#usuarios={}
usuarios = {
    "chaves"   : ["Chaves do 8"    , "24/12/2023", "Recep-01"],
    "kiko"     : ["Kiko do 42"     , "01/01/2024", "XPT-02"  ],
    "chiquinha": ["Chiquinha do 31", "10/01/2024", "Bar-01"  ]       
            }

#imprimindo o dicionario
print(usuarios)

#chamando a função perguntar do funcoes
opcao = perguntar()

#laço de repetição
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I": 
        inserir(usuarios)
        opcao = input(perguntar())
    if opcao=="P":
        pesquisar(usuarios,input("Qual login deseja pesquisar? "))
        opcao = input(perguntar())
    if opcao == "E":
        excluir(usuarios,input("Qual login deseja excluir? "))
        opcao = input(perguntar())
    if opcao == "L":
        listar(usuarios)
        opcao = input(perguntar())
    
