# o r significa read
with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)