#criando um dicionario
usuarios = {}


#atribuindo itens ao dicionario (valor de id : caracteristicas e variaveis deste id)
usuarios = {
    "chaves"   : ["Chaves do 8"    , "24/12/2023", "Recep-01"],
    "kiko"     : ["Kiko do 42"     , "01/01/2024", "XPT-02"  ],
    "chiquinha": ["Chiquinha do 31", "10/01/2024", "Bar-01"  ]       
            }

#imprimindo o dicionario
print(usuarios)

#adicionando um usuário
usuarios["florinda"] = ["Dona Florinda", "12/01/2024", "Cof-01"]

#imprimindo o dicionario
print(usuarios)

print("------------------------------------------#########################################------------------------------------------------------")

#buscando apenas um usuario - metodo get
print(usuarios.get("chiquinha"))
