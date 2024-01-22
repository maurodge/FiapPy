import json

with open("bancodados.json", "r") as json_file:
    dicionario = json.load(json_file)
    print (dicionario)

    #codigo completo, acima o codigo resumido
    #for chave,dados in dicionario.items():
    #    print(chave + " | " + str(dados))
